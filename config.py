from urllib.parse import quote_plus

password = quote_plus("rishabh@#123")

class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://root:{password}@localhost/users"
    SQLALCHEMY_TRACK_MODIFICATIONS = False