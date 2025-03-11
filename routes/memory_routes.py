from flask import Blueprint, request, jsonify, render_template
from textblob import TextBlob
from ..models import db, Memory

memory_bp = Blueprint('memory', __name__)

@memory_bp.route('/')
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

@memory_bp.route('/memories', methods=['POST'])
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

@memory_bp.route('/memories', methods=['GET'])
def get_memories():
    memories = Memory.query.all()
    return jsonify([{'id': m.id, 'text': m.text, 'sentiment': m.sentiment} for m in memories])