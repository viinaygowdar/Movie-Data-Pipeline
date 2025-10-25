# Data Engineering Freshers Assignment: Movie Data Pipeline

## 1. Overview
[cite_start]This project implements an Extract, Transform, Load (ETL) pipeline to ingest movie and rating data from the MovieLens "small" dataset and enrich it with details from the OMDb API[cite: 8]. [cite_start]The cleaned and enriched data is then loaded into an **Oracle Database** for analytical querying[cite: 47]. [cite_start]The entire ingestion and transformation logic is written in **Python**[cite: 19].

## 2. Setup and Execution Instructions

### Prerequisites
1.  **Python 3.x** installed.
2.  **Oracle Database** instance running with the SCOTT/TIGER user (as configured in `etl.py`).
3.  **Required Python Libraries:** Ensure these are installed in your command prompt:
    ```bash
    pip install pandas requests sqlalchemy oracledb
    ```

### Running the Pipeline
1.  [cite_start]Ensure all required files (`etl.py`, `schema.sql`, `queries.sql`, `movies.csv`, `ratings.csv`) are placed in the same directory[cite: 59, 60, 61, 62, 63, 64].
2.  [cite_start]Ensure your Oracle DSN and OMDb API key are correctly set in the `etl.py` file.
3.  **Execute the ETL script** from your command prompt after navigating to the project folder:
    ```bash
    python etl.py
    ```
    [cite_start]*Note: The script implements a delay between API calls to respect OMDb rate limits. The run will take several minutes.*

### Running Analytical Queries
Once the ETL script completes, log into your Oracle SQL Plus session and run the `queries.sql` file:
```sql
@queries.sql