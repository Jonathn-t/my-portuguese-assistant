# app/insert_data.py

from app.database import SessionLocal
from app.models import Lesson

session = SessionLocal()

lesson1 = Lesson(title='Introduction au portugais', content='Bonjour se dit "Olá" en portugais.')
lesson2 = Lesson(title='Les salutations', content='Bonsoir se dit "Boa noite" en portugais.')
lesson3 = Lesson(title='Les bases', content='Merci se dit "Obrigado" en portugais.')

session.add_all([lesson1, lesson2, lesson3])
session.commit()
session.close()

print("Données de test insérées avec succès.")
