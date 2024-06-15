import React from 'react';
import { Link } from 'react-router-dom';

const Menu = () => {
  return (
    <nav>
      <ul>
        <li><Link to="/manage-library">Gestionar Biblioteca Personal</Link></li>
        <li><Link to="/search-books">Buscar Libros</Link></li>
      </ul>
    </nav>
  );
};

export default Menu;
