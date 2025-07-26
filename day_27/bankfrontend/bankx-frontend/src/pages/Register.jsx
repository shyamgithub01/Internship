import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '../api/client';

export default function Register() {
  const [fullName, setFullName] = useState('');
  const [email, setEmail] = useState('');
  const [age, setAge] = useState('');
  const [aadhar, setAadhar] = useState('');
  const [mobile, setMobile] = useState('');
  const [password, setPassword] = useState('');
  const [accountType, setAccountType] = useState('savings');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Basic validation
    if (aadhar.length !== 12 || mobile.length !== 10 || password.length < 8) {
      alert('Please ensure:\n- Aadhar is 12 digits\n- Mobile is 10 digits\n- Password is at least 8 characters');
      return;
    }

    try {
      await api.post('/accounts', {
        full_name: fullName,
        email,
        age: parseInt(age, 10),
        aadhar_card_number: aadhar,
        mobile_number: mobile,
        password,
        account_type: accountType,
      });
      alert('Registration successful!');
      navigate('/login');
    } catch (err) {
      console.error('Backend Error:', err.response?.data);
      alert(err.response?.data?.detail || 'Registration failed');
    }
  };

  return (
    <>
      <form className="register-form" onSubmit={handleSubmit}>
        <h2 className="form-title">Register</h2>

        <label className="form-label">Full Name</label>
        <input type="text" value={fullName} onChange={(e) => setFullName(e.target.value)} required className="form-input" />

        <label className="form-label">Email</label>
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required className="form-input" />

        <label className="form-label">Age</label>
        <input type="number" value={age} onChange={(e) => setAge(e.target.value)} min="18" required className="form-input" />

        <label className="form-label">Aadhar Card #</label>
        <input type="text" value={aadhar} onChange={(e) => setAadhar(e.target.value)} minLength={12} maxLength={12} required className="form-input" />

        <label className="form-label">Mobile Number</label>
        <input type="text" value={mobile} onChange={(e) => setMobile(e.target.value)} minLength={10} maxLength={10} required className="form-input" />

        <label className="form-label">Password</label>
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} minLength={8} required className="form-input" />

        <label className="form-label">Account Type</label>
        <select value={accountType} onChange={(e) => setAccountType(e.target.value)} className="form-input">
          <option value="savings">Savings</option>
          <option value="current">Current</option>
        </select>

        <button type="submit" className="form-button">Register</button>
      </form>

      <style>{`
        .register-form {
          max-width: 500px;
          margin: 2rem auto;
          padding: 2rem;
          background-color: #f9fafb;
          border: 1px solid #e5e7eb;
          border-radius: 8px;
          font-family: sans-serif;
        }

        .form-title {
          text-align: center;
          font-size: 1.75rem;
          font-weight: bold;
          margin-bottom: 1.5rem;
          color: #111827;
        }

        .form-label {
          display: block;
          margin-bottom: 0.4rem;
          font-weight: 600;
          color: #374151;
          font-size: 0.95rem;
        }

        .form-input {
          width: 95%;
          padding: 0.6rem 0.8rem;
          margin-bottom: 1.2rem;
          border: 1px solid #d1d5db;
          border-radius: 4px;
          font-size: 1rem;
          color: #111827;
          background-color: white;
        }

        .form-input:focus {
          border-color: #3b82f6;
          outline: none;
        }

        .form-button {
          width: 100%;
          padding: 0.75rem;
          font-size: 1rem;
          font-weight: 600;
          color: white;
          background-color: #3b82f6;
          border: none;
          border-radius: 4px;
          cursor: pointer;
        }

        .form-button:focus {
          outline: none;
        }

        @media (prefers-color-scheme: dark) {
          .register-form {
            background-color: #1f2937;
            border: 1px solid #374151;
          }

          .form-title {
            color: #f3f4f6;
          }

          .form-label {
            color: #d1d5db;
          }

          .form-input {
            background-color: #111827;
            color: #f9fafb;
            border-color: #4b5563;
          }

          .form-input:focus {
            border-color: #60a5fa;
          }

          .form-button {
            background-color: #2563eb;
          }
        }
      `}</style>
    </>
  );
}
