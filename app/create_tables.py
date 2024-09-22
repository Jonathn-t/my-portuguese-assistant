# app/create_tables.py

from app.database import Base, engine
from app import models

print("Création des tables dans la base de données...")
Base.metadata.create_all(bind=engine)
print("Tables créées avec succès.")
