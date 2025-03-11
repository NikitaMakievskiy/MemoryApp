from flask import Flask
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

# Импорт маршрутов
from routes.memory_routes import memory_bp
app.register_blueprint(memory_bp)

if __name__ == '__main__':
    app.run(debug=True)