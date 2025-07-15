// Child.js
import React, { useContext } from 'react';
import UserContext from './UserContext';

function Child() {
  const name = useContext(UserContext);

  return <h1>Hello, {name}!</h1>;
}

export default Child;
