import pymysql

from app import app
from config import Config
from extensions import db


def create_database():
    connection = pymysql.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_RAW_PASSWORD
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Config.DB_NAME}")
        connection.commit()
    finally:
        connection.close()


if __name__ == "__main__":
    create_database()

    with app.app_context():
        db.create_all()

    print("Database and tables created successfully")
