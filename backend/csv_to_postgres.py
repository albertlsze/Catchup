import json
import functools
from sqlalchemy import create_engine
from pathlib import Path
import pandas as pd

# Get the directory where api_calls.py is located
BASE_DIR = Path(__file__).resolve().parent.parent

def get_credentials()->None:
    # open credential file
    print(f'{BASE_DIR}/Database/postgres_credentials.json')
    with open(f'{BASE_DIR}/Database/postgres_credentials.json', 'r') as f:
        return json.load(f)

def db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        creds = get_credentials()

        # create connection string
        db_url = db_url = f"postgresql://postgres:{creds['password']}@localhost:{creds['port']}/{creds['database']}"

        # create connection
        engine = create_engine(db_url)

        try:
            # Pass the engine as an argument to the function
            return func(engine, *args, **kwargs)
        finally:
            # Dispose of the engine connection pool
            engine.dispose()
            print("Database connection closed.")

    return wrapper

@db_connection
def load_csv_as_raw(engine, file_path:str, db_schema_name: str):
    # read in csv file
    df = pd.read_csv(file_path)

    print(f"Read {len(df)} rows from {file_path}")

    # 3. Write to Postgres
    # name: the table name in Postgres
    # if_exists='replace': Drops the table and recreates it (ideal for raw landing zones)
    # index=False: We don't want the pandas index as a column
    df.to_sql(
        name = db_schema_name,
        con = engine,
        if_exists = 'replace',
        index = False
    )

    print(f"Successfully loaded '{db_schema_name}' to the database.")

if __name__ == "__main__":
    file_path = f"{BASE_DIR}/Database/raw/contact_log.csv"
    db_schema_name = 'raw_contact_log'
    load_csv_as_raw(file_path, db_schema_name)

    file_path = f"{BASE_DIR}/Database/raw/member_contacts.csv"
    db_schema_name = 'raw_member_contacts'
    load_csv_as_raw(file_path, db_schema_name)

    file_path = f"{BASE_DIR}/Database/raw/members.csv"
    db_schema_name = 'raw_members'
    load_csv_as_raw(file_path, db_schema_name)

    file_path = f"{BASE_DIR}/Database/raw/type_of_contact.csv"
    db_schema_name = 'raw_type_of_contact'
    load_csv_as_raw(file_path, db_schema_name)