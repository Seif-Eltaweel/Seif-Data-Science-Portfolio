
import pandas as pd
from sqlalchemy import create_engine

# Function to create a database engine
def create_db_engine(db_url="sqlite:///agriculture.db"):
    return create_engine(db_url)

# Function to query data from a database
def query_data(engine, query):
    with engine.connect() as connection:
        return pd.read_sql(query, connection)

# Function to read a CSV from a web source
def read_from_web_CSV(url):
    return pd.read_csv(url)
