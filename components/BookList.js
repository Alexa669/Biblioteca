import React from 'react';

const BookList = ({ books, onAddBook }) => {
  return (
    <div>
      <h1>Lista de Libros</h1>
      <ul>
        {books.map(book => (
          <li key={book.id}>
            {book.title} - {book.authors}
            <button onClick={() => onAddBook(book.id)}>Añadir a Mi Biblioteca</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BookList;
