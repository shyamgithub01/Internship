import api from './axios';

export const login = async (username, password) => {
  const response = await api.post('/login', {
    username,
    password,
  });
  return response.data.access_token; 
};

const token = await login('your_username', 'your_password');
localStorage.setItem('token', token);
