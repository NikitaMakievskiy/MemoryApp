from flask import Flask, request, jsonify, render_template
from textblob import TextBlob
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:745969mak@localhost/memories_db?client_encoding=utf8'
db = SQLAlchemy(app)

# Модель данных
class Memory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.Float, nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Создание базы данных
with app.app_context():
    db.create_all()

# Главная страница
@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Поделись воспоминанием</title>
    </head>
    <body>
        <h1>Поделись своим воспоминанием</h1>
        <form action="/memories" method="post" enctype="multipart/form-data">
            <textarea name="text" rows="4" cols="50" placeholder="Введите ваше воспоминание..."></textarea><br>
            <button type="submit">Отправить</button>
        </form>
    </body>
    </html>
    '''

# API для загрузки воспоминаний
@app.route('/memories', methods=['POST'])
def add_memory():
    if request.content_type == 'application/json':
        data = request.get_json()
        text = data.get('text')
    else:
        text = request.form.get('text')
    
    if not text:
        return jsonify({'error': 'Text is required'}), 400
    
    sentiment = TextBlob(text).sentiment.polarity  # Анализ тональности
    memory = Memory(text=text, sentiment=sentiment)
    db.session.add(memory)
    db.session.commit()
    
    return jsonify({'message': 'Memory added!', 'sentiment': sentiment}), 201


# API для получения всех воспоминаний
@app.route('/memories', methods=['GET'])
def get_memories():
    memories = Memory.query.all()
    return jsonify([{'id': m.id, 'text': m.text, 'sentiment': m.sentiment} for m in memories])



if __name__ == '__main__':
    app.run(debug=True)