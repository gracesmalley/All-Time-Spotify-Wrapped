# Imports Spotify listening history JSON files into PostgreSQL (keeping in case I need to re-import).

import os
import json
import pandas as pd
from sqlalchemy import create_engine
from config import DATABASE_URL

# Path to extracted JSON files
data_dir = r"C:\Users\grace\Downloads\my_spotify_data\Spotify Extended Streaming History"

# Create database connection
engine = create_engine(DATABASE_URL)


def load_json_files(directory):
    """Loads and merges multiple Spotify history JSON files into a DataFrame."""
    all_data = []

    for file in os.listdir(directory):
        if file.endswith(".json") and "Audio" in file:  # Only process audio history files
            file_path = os.path.join(directory, file)
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                all_data.extend(data)

    return pd.DataFrame(all_data)


def transform_data(df):
    """Transforms raw JSON data into a structured format for PostgreSQL."""
    return df.rename(columns={
        "ts": "played_at",
        "master_metadata_track_name": "track_name",
        "master_metadata_album_artist_name": "artist_name",
        "master_metadata_album_album_name": "album_name",
        "ms_played": "duration_ms",
        "platform": "platform",
        "skipped": "skipped",
        "shuffle": "shuffle",
        "spotify_track_uri": "spotify_uri"
    })[[
        "played_at", "track_name", "artist_name", "album_name", "duration_ms", "platform", "skipped", "shuffle",
        "spotify_uri"
    ]]


def save_to_postgres(df):
    """Saves the DataFrame to PostgreSQL."""
    try:
        df.to_sql("listening_history", con=engine, if_exists="replace", index=False, method="multi")
        print("Listening history successfully saved to database!")
    except Exception as e:
        print(f"Error saving to database: {e}")


if __name__ == "__main__":
    print("Loading Spotify history JSON files...")
    df_raw = load_json_files(data_dir)
    print(f"Loaded {len(df_raw)} records.")

    print("Transforming data...")
    df_transformed = transform_data(df_raw)

    print("Saving data to PostgreSQL...")
    save_to_postgres(df_transformed)
    print("Data import complete!")
