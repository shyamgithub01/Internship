// src/api/user.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'https://fastapi-project-industry-standards-9.onrender.com',
 // Change this to your backend URL
});

// ✅ GET USERS
export const getUsers = async () => {
  try {
    const response = await api.get('/users/id');
    return response.data;
  } catch (error) {
    console.error('Error fetching users:', error);
    return [];
  }
};

// ✅ CREATE USER
export const createUser = async (userData) => {
  try {
    const response = await api.post('/users/id', userData);
    return response.data;
  } catch (error) {
    console.error('Error creating user:', error);
    throw error;
  }
};
