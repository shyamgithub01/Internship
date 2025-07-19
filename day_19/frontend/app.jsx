import { useState } from "react";

function App() {
  const [user, setUser] = useState(null);
  const [error, setError] = useState("");

  const fetchUser = async () => {
    setError(""); // Clear previous error
    setUser(null); // Optional: Clear previous user

    try {
      const response = await fetch("https://jsonplaceholder.typicode.com/users/999"); // try ID 1 for success

      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }

      const data = await response.json();
      setUser(data);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div style={{ padding: "1rem" }}>
      <h2>API Error Handling</h2>
      <button onClick={fetchUser}>Fetch User</button>

      {user && (
        <div>
          <p><strong>Name:</strong> {user.name}</p>
          <p><strong>Email:</strong> {user.email}</p>
        </div>
      )}

      {error && <p style={{ color: "red" }}>Error: {error}</p>}
    </div>
  );
}

export default App;
