# Spotify Listening History Analysis

This project analyzes a user's full Spotify listening history using their official data archive. It uses PostgreSQL to store data and generates clean, Spotify-styled visualizations of top songs and artists.

## Project Overview

The data was downloaded through Spotify’s Privacy Data portal and includes extended streaming history in JSON format. This project processes that data through several Python scripts to load, structure, store, and visualize listening trends.

### 1. `import_spotify_json.py`
- Loads all extended Spotify streaming history `.json` files.
- Filters only audio streaming records.
- Renames and restructures fields for database compatibility.
- Saves the transformed data to a PostgreSQL table named `listening_history`.

### 2. `database.py`
- Manages the PostgreSQL database connection using SQLAlchemy.
- Provides a reusable `save_to_db()` function for storing any DataFrame.

### 3. `config.py`
- Stores environment-safe PostgreSQL connection settings.
- Constructs the full database URL used across all scripts.

### 4. `visualization.py`
- Connects to the database and fetches the top 10 most played tracks and artists.
- Uses Matplotlib and Seaborn to generate horizontal bar charts styled with Spotify’s color palette.
- Includes functions to generate separate charts for top songs and top artists.

### 5. `main.py`
- Entry point that runs the visualization pipeline.
- Imports and calls `generate_visualizations()` from `visualization.py`.

## Dependencies
- pandas  
- matplotlib  
- seaborn  
- sqlalchemy  
- psycopg2  
- PostgreSQL (as the backend database)

## How to Run

1. Download your Spotify data archive from: https://www.spotify.com/account/privacy/
2. Extract it and update the `data_dir` path in `import_spotify_json.py`.
3. Make sure PostgreSQL is running and credentials in `config.py` are correct.
4. Run the scripts in order:
```bash
python import_spotify_json.py   # Load and store listening history
python main.py                  # Generate top artists and songs charts

Grace Smalley – Bridgewater State University
Spotify Wrapped Project | Spring 2025
