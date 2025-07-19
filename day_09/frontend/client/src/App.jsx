import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Home from "./Home";
import About from "./About";
import Contact from "./Contact";
import Goal from "./Goal";
import Team from "./Team";
import User from "./User";

function App() {
  return (
    <>
      <BrowserRouter>
        <nav className="nab-bar" >
          <Link to="/">Home</Link>
          <Link to="/about">About</Link>
          <Link to="/contact">Contact</Link>
          <Link to="/user/101">User 101</Link>
          <Link to="/user/102">User 102</Link>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />}>
            <Route path="team" element={<Team />} />
            <Route path="goal" element={<Goal />} />
          </Route>

          <Route path="/contact" element={<Contact />} />
          <Route path="/user/:id" element={<User/>}/>
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
