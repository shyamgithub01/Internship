import { useState } from 'react';

function MyForm() {
  const [name, setName] = useState(""); // state to hold the value

  const handleChange = (e) => {
    setName(e.target.value); // update state when input changes
  };

  const handleSubmit = (e) => {
    e.preventDefault(); // prevent page reload
    alert(`Hello, ${name}!`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>Enter your name: </label>
      <input type="text" value={name} onChange={handleChange} />
      <button type="submit">Submit</button>
    </form>
  );
}

export default MyForm;
