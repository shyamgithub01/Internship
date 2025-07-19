// App.js
import React from 'react';
import UserContext from './UserContext';
import Child from './Child';

function App() {
  const username = "Shyam";

  return (
    <UserContext.Provider value={username}>
      <Child />
    </UserContext.Provider>
  );
}

export default App;
