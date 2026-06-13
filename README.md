\# 🎬 Movie Data Pipeline



> An \*\*ETL (Extract, Transform, Load) pipeline\*\* that ingests movie data from MovieLens, enriches it with real-time OMDb API data, cleans it, and loads it into a SQLite database for analytics.



!\[Python](https://img.shields.io/badge/Python-3.8+-blue) !\[SQLite](https://img.shields.io/badge/Database-SQLite-green) !\[API](https://img.shields.io/badge/API-REST-orange)



\## 📊 Quick Overview



| Metric | Value |

|--------|-------|

| \*\*Data Source\*\* | MovieLens Dataset + OMDb API |

| \*\*Records Processed\*\* | 300+ movies |

| \*\*API Calls\*\* | 300+ with throttling |

| \*\*Database\*\* | SQLite |

| \*\*Execution Time\*\* | \~5-7 minutes |



\## 🚀 Features



✅ \*\*Automated ETL Pipeline\*\* — Extract from CSV, enrich via API, load to DB

✅ \*\*Real-time API Enrichment\*\* — Fetches OMDb details

✅ \*\*Smart Data Cleaning\*\* — Handles missing values, duplicates

✅ \*\*SQL Analytics\*\* — Pre-built analytical queries

✅ \*\*Rate-Limit Friendly\*\* — Respects API rate limits

✅ \*\*Idempotent Design\*\* — Safe to re-run anytime



\## ⚡ Quick Start



\### Install Dependencies

```bash

pip install -r requirements.txt

```



\### Run the Pipeline

```bash

python src/etl.py

```



\## 📂 Project Structure

