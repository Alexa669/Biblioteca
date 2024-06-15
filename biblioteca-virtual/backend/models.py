from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    authors = db.Column(db.String(200), nullable=False)
    publisher = db.Column(db.String(200), nullable=False)
    publication_date = db.Column(db.String(50), nullable=False)
    isbn = db.Column(db.String(20), nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    language = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'authors': self.authors,
            'publisher': self.publisher,
            'publication_date': self.publication_date,
            'isbn': self.isbn,
            'pages': self.pages,
            'genre': self.genre,
            'language': self.language
        }

class UserBook(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True)
    status = db.Column(db.String(10), nullable=False, default='unread')
    book = db.relationship(Book)

    def __init__(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id
