# config/settings.py

import os

DATABASE_CONFIG = {
    'dbname': os.getenv('POSTGRES_DB', 'assistant_portugais'),
    'user': os.getenv('POSTGRES_USER', 'admin'),
    'password': os.getenv('POSTGRES_PASSWORD', 'secret123'),
    'host': os.getenv('POSTGRES_HOST', 'db'),  # 'db' pour Docker Compose
    'port': int(os.getenv('POSTGRES_PORT', 5432)),
}
