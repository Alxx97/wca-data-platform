# WCA Data Platform
End-to-end data platform built on top of World Cube Association (WCA) database.
This project covers the full data lifecycle: ingestion, transformation, storage, analytics, and ML-ready datasets.

The initial focus is on building robust data engineering pipeline and generating a curated subset of the data for Mexican competitors.

## Project goals

- Automatically ingest and update the WCA database
- Build reproducible ETL pipelines
- Create a Mexico-only curated dataset
- Design:
  - OLTP schemas (normalized)
  - OLPA schemas (analytics-ready)
- Enable downstream:
  - Dashboards
  - Data analytics
  - ML models
  
## Tech Stack

- **Database**: MariaDB
- **Programming Languange**: Python
- **Data processing**: Pandas, Polars, SQL
- **Analytics / ML**: To be planned

## Data Source

This project uses data from the World Cube Association (WCA).

The WCA data is owned by the World Cube Association and is used here strictly for educational and non-commercial purposes.

## Disclaimer

This project is intended for learning, experimentation, and portfolio purposes.
It is not affiliated with or endorsed by the World Cube Association.

## License

This project is licensed under the MIT License.
