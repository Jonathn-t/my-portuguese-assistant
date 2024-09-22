# config/settings.py

import os

DATABASE_CONFIG = {
    'dbname': os.getenv('POSTGRES_DB', 'default_db_name'),
    'user': os.getenv('POSTGRES_USER', 'default_username'),
    'password': os.getenv('POSTGRES_PASSWORD', 'default_password'),
    'host': 'db',
    'port': 5432,
}
