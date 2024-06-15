import React from 'react';

const BookDetails = ({ book, onMarkAsRead, onRemove }) => {
  return (
    <div>
      <h2>{book.title}</h2>
      <p>Autor(es): {book.authors}</p>
      <p>Editorial: {book.publisher}</p>
      <p>Fecha de publicación: {book.publication_date}</p>
      <p>ISBN: {book.isbn}</p>
      <p>Número de páginas: {book.pages}</p>
      <p>Género: {book.genre}</p>
      <p>Idioma: {book.language}</p>
      <p>Estado: {book.status}</p>
      <button onClick={() => onMarkAsRead(book.id, book.status === 'read' ? 'unread' : 'read')}>
        {book.status === 'read' ? 'Marcar como No Leído' : 'Marcar como Leído'}
      </button>
      <button onClick={() => onRemove(book.id)}>Eliminar</button>
    </div>
  );
};

export default BookDetails;
