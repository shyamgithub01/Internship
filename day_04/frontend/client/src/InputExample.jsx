import { useState } from 'react';

function InputExample() {
  const [text, setText] = useState("");

  const handleChange = (e) => {
    setText(e.target.value);
  };

  return (
    <>
      <input type="text" onChange={handleChange} />
      <p>You typed: {text}</p>
    </>
  );
}

export default InputExample