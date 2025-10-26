# Data Engineering Freshers Assignment: Movie Data Pipeline

## 1. Overview
[cite_start]This project implements an **Extract, Transform, Load (ETL) pipeline** to ingest movie and rating data from the MovieLens "small" dataset [cite: 23, 24] [cite_start]and enrich it with details from the OMDb API[cite: 26, 27]. [cite_start]The transformation logic is written entirely in **Python** [cite: 19][cite_start], and the final cleaned data is loaded into a **SQLite Database** file[cite: 17].

## 2. Setup and Execution Instructions

### Prerequisites
1.  **Python 3.x** installed.
2.  **Required Python Libraries:** Ensure these are installed in your command prompt:
    ```bash
    pip install pandas requests sqlalchemy
    ```

### Running the Pipeline
1.  Ensure all required files (`etl.py`, `movies.csv`, `ratings.csv`, `queries.sql`, `README.md`) are placed in the same directory.
2.  **Execute the ETL script** from your command prompt after navigating to the project folder:
    ```bash
    "C:\Users\vinay\anaconda3\python.exe" etl.py
    ```
    *Note: The script is intentionally limited to process the first **300 movies** and implements a delay between API calls to respect the OMDb rate limits. The run will take several minutes.*

### Running Analytical Queries
Once the ETL script completes and the `movies_data.db` file is created:
1.  Connect to the database using the SQLite command-line tool:
    ```bash
    sqlite3 movies_data.db
    ```
2.  Run the analytical queries from the prompt:
    ```sqlite
    .read queries.sql
    ```

## 3. Technical Design and Choices

| Component | Choice | Rationale |
| :--- | :--- | :--- |
| **Database** | **SQLite** | [cite_start]Switched from the originally recommended server-based options [cite: 17] to **SQLite** to eliminate persistent network/connection errors, providing a simple and highly reproducible submission. |
| **Data Modeling** | **Flattened Schema** | The final structure is a single **`MOVIES`** table, consolidating movie details, API enrichment, and calculated average rating. This simplifies the loading process and speeds up the required analytical queries (Task 5). |
| **Idempotency** | **Replace-and-Load** | [cite_start]The Python script uses `if_exists='replace'` when loading data into SQLite[cite: 48]. This ensures re-running the pipeline clears the old data and inserts fresh data without creating duplicate entries. |

## 4. Challenges and Solutions

1.  [cite_start]**OMDb API Rate Limiting (Task 4):** The free OMDb API has a low daily request limit[cite: 28].
    * [cite_start]**Solution:** The ETL process was intentionally throttled using **`.head(300)`** to limit the data size and a **`time.sleep(0.2)`** delay between API calls, ensuring the pipeline completes successfully[cite: 39].
2.  **SQL Syntax Mismatch (Task 5):** The original design used Oracle syntax (`FETCH FIRST N ROWS`).
    * **Solution:** The **`queries.sql`** file was corrected to use the standard **SQLite `LIMIT N`** syntax for compatibility.
3.  [cite_start]**Data Cleaning:** Handled title parsing using regular expressions and filtered out movies that failed the API lookup (`NoneType` error)[cite: 41, 43].