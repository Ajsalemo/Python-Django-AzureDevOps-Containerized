import os

# Environment variables defined in one from to act as a module and export/import as needed
POSTGRES_ENGINE = os.getenv('POSTGRES_ENGINE')
POSTGRES_NAME = os.getenv('POSTGRES_NAME')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')

UNSPLASH_API_PREFIX = os.getenv('UNSPLASH_API_PREFIX')
UNSPLASH_API_ACCESS_KEY = os.getenv('UNSPLASH_API_ACCESS_KEY')
UNSPLASH_API_SECRET_KEY = os.getenv('UNSPLASH_API_SECRET_KEY')
