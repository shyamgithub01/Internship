import React, { useEffect, useState } from "react";
import axios from "axios";

const Dashboard = () => {
  const [balance, setBalance] = useState(null);
  const [formData, setFormData] = useState({
    email: "",
    password: ""
  });

  useEffect(() => {
    // Fetch balance on load (if needed)
    // Commented out since GET /accounts/ is not allowed
    // load();
  }, []);

  const loadBalance = () => {
    axios
      .get("http://localhost:8000/accounts/balance", {
        params: formData
      })
      .then((res) => setBalance(res.data.balance))
      .catch((err) => console.error(err));
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Bank Account Dashboard</h2>
      <div style={{ marginBottom: "1rem" }}>
        <input
          type="email"
          name="email"
          placeholder="Email"
          onChange={handleChange}
          style={{ padding: "0.5rem", marginRight: "0.5rem" }}
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          onChange={handleChange}
          style={{ padding: "0.5rem", marginRight: "0.5rem" }}
        />
        <button onClick={loadBalance} style={{ padding: "0.5rem" }}>
          Get Balance
        </button>
      </div>
      {balance !== null && <p>Balance: ₹{balance}</p>}
    </div>
  );
};

export default Dashboard;
