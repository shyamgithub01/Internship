import { useState, useEffect } from 'react';

function App() {
  const [users, setUsers] = useState([]);
  const [formData, setFormData] = useState({ id: '', name: '', email: '' });

  // Fetch users from backend
  const fetchUsers = async () => {
    const res = await fetch('http://localhost:8000/users');
    const data = await res.json();
    setUsers(data);
  };

  // Handle input change
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // Handle form submit
  const handleSubmit = async (e) => {
    e.preventDefault();

    await fetch('http://localhost:8000/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        id: Number(formData.id),
        name: formData.name,
        email: formData.email,
      }),
    });

    setFormData({ id: '', name: '', email: '' });
    fetchUsers(); // Refresh the user list
  };

  // Fetch users on first load
  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h2>User Form</h2>
      <form onSubmit={handleSubmit}>
        <input
          name="id"
          type="number"
          placeholder="ID"
          value={formData.id}
          onChange={handleChange}
          required
        />
        <input
          name="name"
          placeholder="Name"
          value={formData.name}
          onChange={handleChange}
          required
        />
        <input
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <button type="submit">Add User</button>
      </form>

      <h3>User List</h3>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            {user.name} ({user.email})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
