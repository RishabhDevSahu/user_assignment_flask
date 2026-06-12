import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_USER = os.getenv("DB_USER", "root")
    DB_RAW_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_PASSWORD = quote_plus(DB_RAW_PASSWORD)
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_NAME = os.getenv("DB_NAME", "users")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
