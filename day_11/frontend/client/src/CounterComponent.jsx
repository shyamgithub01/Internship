// CounterComponent.js
import React from "react";
import useCounter from './useCounter'


function CounterComponent() {
  const { count, increment, decrement, reset } = useCounter(5);

  return (
    <div>
      <h2>Count: {count}</h2>
      <button onClick={increment}>➕</button>
      <button onClick={decrement}>➖</button>
      <button onClick={reset}>🔁</button>
    </div>
  );
}

export default CounterComponent;
