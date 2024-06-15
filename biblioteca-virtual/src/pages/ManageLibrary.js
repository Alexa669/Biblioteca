import React, { useState, useEffect } from 'react';
import { getUserBooks, removeUserBook, markBookAsRead } from '../api/api';

const ManageLibrary = ({ userId }) => {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    const fetchBooks = async () => {
      const userBooks = await getUserBooks(userId);
      setBooks(userBooks);
    };
    fetchBooks();
  }, [userId]);

  const handleRemove = async (bookId) => {
    await removeUserBook(userId, bookId);
    setBooks(books.filter(book => book.id !== bookId));
  };

  const handleMarkAsRead = async (bookId, status) => {
    await markBookAsRead(userId, bookId, status);
    setBooks(books.map(book => book.id === bookId ? { ...book, status } : book));
  };

  return (
    <div>
      <h1>Mi Biblioteca Personal</h1>
      <ul>
        {books.map(book => (
          <li key={book.id}>
            {book.title} - {book.status}
            <button onClick={() => handleMarkAsRead(book.id, book.status === 'read' ? 'unread' : 'read')}>
              {book.status === 'read' ? 'Marcar como No Leído' : 'Marcar como Leído'}
            </button>
            <button onClick={() => handleRemove(book.id)}>Eliminar</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ManageLibrary;
