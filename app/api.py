# app/api.py

from flask import Flask, jsonify, render_template
from app.database import SessionLocal
from app.models import Lesson

app = Flask(__name__)

@app.route('/')
def home():
    session = SessionLocal()
    lessons = session.query(Lesson).all()
    session.close()
    return render_template('index.html', lessons=lessons)

@app.route('/api/lessons', methods=['GET'])
def get_lessons():
    session = SessionLocal()
    lessons = session.query(Lesson).all()
    session.close()
    lessons_data = [{'id': lesson.id, 'title': lesson.title, 'content': lesson.content} for lesson in lessons]
    return jsonify(lessons_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
