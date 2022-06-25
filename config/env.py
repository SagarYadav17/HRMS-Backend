from os import environ
from dotenv import load_dotenv

load_dotenv()

# Django
DJAGNO_DEBUG = environ.get("DEBUG", False)
DJANGO_SECRET_KEY = environ.get("SECRET_KEY", "secret")

# Database
DB_NAME = environ.get("DB_NAME", "hrms")
DB_USER = environ.get("DB_USER", "postgres")
DB_PASSWORD = environ.get("DB_PASSWORD", "postgres")
DB_HOST = environ.get("DB_HOST", "localhost")
DB_PORT = environ.get("DB_PORT", "5432")
