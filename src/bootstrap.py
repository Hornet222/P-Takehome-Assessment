# This file is where you will bootstrap your Postgres instance.

## connect to posgresql

## create table in public database

import logging
import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, Table, Column, String, Float, Text, UniqueConstraint,text

load_dotenv()
# Setup logging
logging.basicConfig(filename='/logs/logfile.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
logger = logging.getLogger()

# Reading environment variables 
DATABASE_URL = os.getenv('DATABASE_URL')
TARGET_DB_NAME = os.getenv('TARGET_DB_NAME')
DATABASE_URL_BASE = DATABASE_URL.replace(TARGET_DB_NAME,'postgres')

# Function to check and create the database if it doesn't exist
def ensure_database_exists(engine, db_name):
    with engine.connect() as conn:
        existing_databases = conn.execute(text("SELECT datname FROM pg_database;")).fetchall()
        if (db_name,) not in existing_databases:
            conn.execute(text(f"CREATE DATABASE {db_name}"))
            logger.info(f"Database {db_name} created!")
        else:
            logger.info(f"Database {db_name} already exists!")



if __name__ == '__main__':
    # default to 'postgres' db for initial connection
    ensure_database_exists(create_engine(DATABASE_URL_BASE), TARGET_DB_NAME)

    # Once the database is created or verified to exist, set the engine to the target database
    engine = create_engine(DATABASE_URL)
    metadata = MetaData()

    # Define the employees table
    employees = Table(
        'employees', metadata,
        Column('employeeId', String, primary_key=True),
        Column('name', String),
        UniqueConstraint('employeeId')
    )

    # Define the expenses table
    expenses = Table(
        'expenses', metadata,
        Column('transactionId', String, primary_key=True),
        Column('cost', Float),
        Column('metadata', Text),
        UniqueConstraint('transactionId')
    )

    # Create the tables
    metadata.create_all(engine)


    logger.info("Tables created successfully!")

