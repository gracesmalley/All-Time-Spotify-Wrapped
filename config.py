# This script stores database connection settings for PostgreSQL
import os

DB_USER = os.getenv("POSTGRES_USER", "spotify_user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "T0bey.b0y17!")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "spotify_wrapped")

# Construct database URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
