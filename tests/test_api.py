# tests/test_api.py

import unittest
from app.api import app
from app.database import Base, engine, SessionLocal
from app.models import Lesson

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        # Réinitialiser la base de données pour les tests
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        session = SessionLocal()
        lesson = Lesson(title='Test Lesson', content='Contenu de la leçon de test.')
        session.add(lesson)
        session.commit()
        session.close()

    def tearDown(self):
        # Supprimer les données après chaque test
        Base.metadata.drop_all(bind=engine)

    def test_get_lessons(self):
        response = self.app.get('/api/lessons')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], 'Test Lesson')

if __name__ == '__main__':
    unittest.main()
