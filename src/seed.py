# This file is where you will seed your Postgres database with the sample data from the data directory.

import os
import pandas as pd
import logging
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(filename='/logs/logfile.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
logger = logging.getLogger()

load_dotenv()

# Reading environment variables
DATABASE_URL = os.getenv('DATABASE_URL')


def seed_data_from_csv(file_path, table_name, engine):
    try:
        # Load CSV data into a DataFrame
        df = pd.read_csv(file_path, delimiter='|')
        
        # Insert data from DataFrame to the database table. Replace existing data if any
        df.to_sql(table_name, engine, if_exists='replace', index=False, chunksize = 1000)
        logger.info(f"Seeded data from {file_path} to {table_name} table.")
        
    except Exception as e:
        print (e)
        logger.error(f"Error seeding data from {file_path} to {table_name}: {str(e)}")

if __name__ == '__main__':
    # Connect to the target database
    engine = create_engine(DATABASE_URL)
    print (os.getcwd())
    # Seed employees data
    seed_data_from_csv('/data/employees.csv', 'employees',engine)
    
    # Seed expenses data
    seed_data_from_csv('/data/expenses.csv', 'expenses',engine)
