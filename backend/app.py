from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

from models import User, Book, UserBook

# Ruta para obtener todos los libros
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

# Ruta para obtener los libros de un usuario
@app.route('/users/<int:user_id>/books', methods=['GET'])
def get_user_books(user_id):
    user_books = UserBook.query.filter_by(user_id=user_id).all()
    return jsonify([ub.book.to_dict() for ub in user_books])

# Ruta para agregar un libro a la biblioteca de un usuario
@app.route('/users/<int:user_id>/books', methods=['POST'])
def add_user_book(user_id):
    data = request.get_json()
    book_id = data.get('book_id')
    if not book_id:
        return jsonify({'error': 'book_id is required'}), 400
    if UserBook.query.filter_by(user_id=user_id, book_id=book_id).first():
        return jsonify({'error': 'Book already in library'}), 400
    new_user_book = UserBook(user_id=user_id, book_id=book_id)
    db.session.add(new_user_book)
    db.session.commit()
    return jsonify({'message': 'Book added to library'}), 201

# Ruta para eliminar un libro de la biblioteca de un usuario
@app.route('/users/<int:user_id>/books/<int:book_id>', methods=['DELETE'])
def remove_user_book(user_id, book_id):
    user_book = UserBook.query.filter_by(user_id=user_id, book_id=book_id).first()
    if not user_book:
        return jsonify({'error': 'Book not found in library'}), 404
    db.session.delete(user_book)
    db.session.commit()
    return jsonify({'message': 'Book removed from library'}), 200

# Ruta para marcar un libro como leído/no leído
@app.route('/users/<int:user_id>/books/<int:book_id>', methods=['PUT'])
def mark_book_as_read(user_id, book_id):
    data = request.get_json()
    status = data.get('status')
    if status not in ['read', 'unread']:
        return jsonify({'error': 'Invalid status'}), 400
    user_book = UserBook.query.filter_by(user_id=user_id, book_id=book_id).first()
    if not user_book:
        return jsonify({'error': 'Book not found in library'}), 404
    user_book.status = status
    db.session.commit()
    return jsonify({'message': 'Book status updated'}), 200

if __name__ == '__main__':
    app.run(debug=True)
