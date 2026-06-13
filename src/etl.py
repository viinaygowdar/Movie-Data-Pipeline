import pandas as pd
import requests
import time
from sqlalchemy import create_engine

DB_URL = 'sqlite:///movies_data.db' 
OMDB_API_KEY = 'b4dcffee'
MOVIE_LIMIT = 300 

def fetch_omdb_data(title, year):
    base_url = "http://www.omdbapi.com/"
    params = {
        't': title,
        'y': year,
        'apikey': OMDB_API_KEY
    }
    
    time.sleep(0.2) 
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data.get('Response') == 'False':
            return None
        
        return {
            'Genre': data.get('Genre'),
            'Director': data.get('Director'),
            'imdbRating': data.get('imdbRating'),
            'Runtime': data.get('Runtime')
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {title} ({year}): {e}")
        return None

def run_etl_pipeline():
    print("--- Starting ETL Pipeline (using SQLite) ---")

    movies_df = pd.read_csv('movies.csv').head(MOVIE_LIMIT) 
    ratings_df = pd.read_csv('ratings.csv')
    
    movies_df['title_clean'] = movies_df['title'].str.replace(r'\s*\(\d{4}\)', '', regex=True).str.strip()
    movies_df['year'] = movies_df['title'].str.extract(r'\((\d{4})\)', expand=False)
    
    omdb_data_list = []
    total_movies = len(movies_df)
    print(f"Fetching OMDb data for {total_movies} movies...")
    
    for index, row in movies_df.iterrows():
        omdb_data = fetch_omdb_data(row['title_clean'], row['year'])
        omdb_data_list.append(omdb_data)
        
        if (index + 1) % 100 == 0:
            print(f"\tProcessed {index + 1}/{total_movies} movies.")
            
    omdb_data_list_cleaned = [data for data in omdb_data_list if data is not None]
    omdb_df = pd.DataFrame(omdb_data_list_cleaned)
    
    movies_full_df = pd.concat([movies_df.reset_index(drop=True), omdb_df], axis=1)

    avg_ratings = ratings_df.groupby('movieId')['rating'].mean().reset_index()
    avg_ratings.rename(columns={'movieId': 'movie_id', 'rating': 'avg_rating'}, inplace=True)
    
    movies_to_load = pd.merge(
        movies_full_df, 
        avg_ratings, 
        left_on='movieId', 
        right_on='movie_id',   
        how='left'
    )
    
    movies_to_load['avg_rating'] = movies_to_load['avg_rating'].fillna(0.0)
    
    movies_to_load = movies_to_load.loc[:, [
        'movieId', 'title_clean', 'year', 'Genre', 'Director', 
        'imdbRating', 'Runtime', 'avg_rating'
    ]]
    movies_to_load.columns = [
        'movie_id', 'title', 'release_year', 'genre', 'director', 
        'imdb_rating', 'runtime', 'avg_rating'
    ]
    
    print("\nLoading data into the SQLite database...")
    
    try:
        engine = create_engine(DB_URL)
        
        movies_to_load.to_sql(
            name='MOVIES', 
            con=engine, 
            if_exists='replace',
            index=False,
            chunksize=500
        )
            
        print("--- ETL Pipeline finished successfully. Data loaded into SQLite DB. ---")
        
    except Exception as e:
        print(f"\n[FATAL ERROR] An unexpected error occurred: {e}")


if __name__ == "__main__":
    run_etl_pipeline()