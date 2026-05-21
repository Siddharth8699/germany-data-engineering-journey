import os
import psycopg2
from dotenv import load_dotenv
from logger_config import logger

# Find the absolute path to config/.env
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_path = os.path.join(BASE_DIR, 'config', '.env')
load_dotenv(dotenv_path)

def get_db_connection():
    """
    Opens a secure pipeline connection to your local PostgreSQL server.
    """
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        logger.info("Successfully connected to the PostgreSQL database.")
        return connection
        
    except psycopg2.OperationalError as e:
        logger.error(f"Database connection failed! Error details: {e}")
        print("❌ Database Connection Error! Check your logs/app.log file.")
        return None