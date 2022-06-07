from os import environ
from dotenv import load_dotenv

load_dotenv()

# Django
DJAGNO_DEBUG = environ.get("DEBUG", False)
DJANGO_SECRET_KEY = environ.get("SECRET_KEY", "secret")

# Auth0
JWT_AUDIENCE = environ.get("JWT_AUDIENCE", "localhost:8000")
JWT_ISSUER = environ.get("JWT_ISSUER", "https://dev-x0ywsv9o.us.auth0.com/")
JWT_ALGORITHM = environ.get("JWT_ALGORITHM", "RS256")

# Database
DB_NAME = environ.get("DB_NAME", "hrms")
DB_USER = environ.get("DB_USER", "postgres")
DB_PASSWORD = environ.get("DB_PASSWORD", "postgres")
DB_HOST = environ.get("DB_HOST", "localhost")
DB_PORT = environ.get("DB_PORT", "5432")
