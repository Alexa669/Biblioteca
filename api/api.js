import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:5000', // URL de tu backend Flask
});

export const getBooks = async () => {
  const response = await api.get('/books');
  return response.data;
};

export const addUserBook = async (userId, bookId) => {
  await api.post(`/users/${userId}/books`, { book_id: bookId });
};

export const getUserBooks = async (userId) => {
  const response = await api.get(`/users/${userId}/books`);
  return response.data;
};

export const removeUserBook = async (userId, bookId) => {
  await api.delete(`/users/${userId}/books/${bookId}`);
};

export const markBookAsRead = async (userId, bookId, status) => {
  await api.put(`/users/${userId}/books/${bookId}`, { status });
};
