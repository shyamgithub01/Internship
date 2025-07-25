import React, { useEffect, useState } from 'react';
import { getUsers } from '../api/user';

function Users() {
  const [users, setUsers] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    getUsers()
      .then(data => {
        console.log("User data:", data);
        if (Array.isArray(data)) {
          setUsers(data); // ✅ should be an array if coming from PostgreSQL
        } else {
          setError("Unexpected data format");
        }
      })
      .catch(err => {
        console.error("Error:", err);
        setError("Failed to fetch users. Check login or API.");
      });
  }, []);

  return (
    <div>
      <h2>Users List</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <ul>
        {users.length > 0 ? (
          users.map(user => (
            <li key={user.id}>
              <strong>{user.email}</strong> — ID: {user.id}
            </li>
          ))
        ) : (
          !error && <li>Loading...</li>
        )}
      </ul>
    </div>
  );
}

export default Users;
