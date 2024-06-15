import React, { useState, useEffect } from 'react';
import { getBooks, addUserBook } from '../api/api';

const SearchBooks = ({ userId }) => {
  const [books, setBooks] = useState([]);
  const [message, setMessage] = useState('');

  useEffect(() => {
    const fetchBooks = async () => {
      const availableBooks = await getBooks();
      setBooks(availableBooks);
    };
    fetchBooks();
  }, []);

  const handleAddBook = async (bookId) => {
    try {
      await addUserBook(userId, bookId);
      setMessage('Libro añadido a tu biblioteca personal.');
    } catch (error) {
      setMessage('El libro ya está en tu biblioteca personal.');
    }
  };

  return (
    <div>
      <h1>Buscar Libros</h1>
      {message && <p>{message}</p>}
      <ul>
        {books.map(book => (
          <li key={book.id}>
            {book.title} - {book.author}
            <button onClick={() => handleAddBook(book.id)}>Añadir a Mi Biblioteca</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SearchBooks;
