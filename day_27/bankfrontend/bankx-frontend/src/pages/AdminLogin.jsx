import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function AdminLogin() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    localStorage.setItem('admin', JSON.stringify({ username, password }));
    navigate('/add-employee');
  };

  return (
    <>
      <form className="admin-login-form" onSubmit={handleSubmit}>
        <h2 className="form-title">Admin Login</h2>

        <div>
          <label className="form-label">Admin Username</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            className="form-input"
          />
        </div>

        <div>
          <label className="form-label">Admin Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            className="form-input"
          />
        </div>

        <button type="submit" className="form-button">Login</button>
      </form>

      <style>{`
        .admin-login-form {
          max-width: 400px;
          margin: 3rem auto;
          background: linear-gradient(135deg, #ffffff, #f0f7ff);
          padding: 2.5rem;
          border-radius: 1.5rem;
          box-shadow: 0 10px 25px rgba(59, 130, 246, 0.25);
          transition: all 0.4s ease;
          transform: perspective(1000px) translateZ(0);
        }

        .admin-login-form:hover {
          transform: perspective(1000px) translateZ(5px) scale(1.02);
          box-shadow: 0 12px 28px rgba(59, 130, 246, 0.4);
        }

        .form-title {
          text-align: center;
          font-size: 1.75rem;
          font-weight: bold;
          margin-bottom: 2rem;
          color: #1e3a8a;
        }

        .form-label {
          display: block;
          margin-bottom: 0.5rem;
          font-weight: 600;
          color: #1d4ed8;
        }

        .form-input {
          width: 100%;
          padding: 0.75rem 1rem;
          margin-bottom: 1.5rem;
          border: 1px solid #93c5fd;
          border-radius: 0.5rem;
          font-size: 1rem;
          color: #1e40af;
          background-color: white;
          transition: all 0.3s ease;
        }

        .form-input:focus {
          border-color: #3b82f6;
          outline: none;
          box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.3);
        }

        .form-button {
          width: 100%;
          padding: 0.9rem;
          font-weight: 600;
          font-size: 1rem;
          color: white;
          background: linear-gradient(to right, #2563eb, #4f46e5);
          border: none;
          border-radius: 0.75rem;
          cursor: pointer;
          box-shadow: 0 4px 12px rgba(79, 70, 229, 0.4);
          transition: all 0.3s ease;
        }

        .form-button:hover {
          background: linear-gradient(to right, #4f46e5, #7c3aed);
          transform: scale(1.05);
          box-shadow: 0 6px 18px rgba(79, 70, 229, 0.5);
        }

        .form-button:active {
          transform: scale(0.97);
        }
      `}</style>
    </>
  );
}
