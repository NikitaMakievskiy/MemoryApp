from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:745969mak@localhost/memories_db?client_encoding=utf8'
db = SQLAlchemy(app)

# Модель данных
class Memory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.Float, nullable=False)

# Создание базы данных
with app.app_context():
    db.create_all()

# API для загрузки воспоминаний
@app.route('/memories', methods=['POST'])
def add_memory():
    data = request.get_json()
    text = data.get('text')
    
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

# Главная страница
@app.route('/')
def home():
    return "Hello, World!"  # Ответ на запрос к главной странице

if __name__ == '__main__':
    app.run(debug=True)