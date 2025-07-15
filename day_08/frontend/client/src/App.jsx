import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from '../pages/Home';
import AddUser from '../pages/AddUser';
import EditUser from '../pages/EditUser';

function App() {
  return (
    <Router>
      <div style={{ padding: '20px' }}>
        {/* ✅ Navigation Links */}
        <nav style={{ marginBottom: '20px' }}>
          <Link to="/" style={{ marginRight: '10px' }}>Home</Link>
          <Link to="/add">Add User</Link>
          <Link to = "/edit/:id" >Edit user</Link>
        </nav>

        {/* ✅ Page Routes */}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/add" element={<AddUser />} />
          <Route path="/edit/:id" element={<EditUser />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
