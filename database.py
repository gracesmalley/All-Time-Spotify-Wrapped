# This script manages database connections and saving data to PostgreSQL
from sqlalchemy import create_engine
from config import DATABASE_URL

# Create the database engine
engine = create_engine(DATABASE_URL)

def save_to_db(df, table_name):
    """Saves a Pandas DataFrame to PostgreSQL."""
    try:
        df.to_sql(table_name, con=engine, if_exists="replace", index=False, method="multi")
        print(f"{table_name} data saved to database!")
    except Exception as e:
        print(f"Error saving to database: {e}")
