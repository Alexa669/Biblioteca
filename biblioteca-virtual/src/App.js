
import './App.css';
import React from 'react';
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Menu from './components/menu';
import ManageLibrary from './pages/ManageLibrary';
import SearchBooks from './pages/SearchBooks';

const App = () => {
  const userId = 1; // Aquí podrías obtener el ID del usuario autenticado

  return (
    <Router>
      <div>
        <Menu />
        <Routes>
        <Route path="/manage-library" element={<ManageLibrary userId={userId} />} />
        <Route path="/search-books" element={<SearchBooks userId={userId} />} />
   
        </Routes>
      </div>
    </Router>
     
  );
};

export default App;
