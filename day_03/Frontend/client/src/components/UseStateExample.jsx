import React, { useState } from 'react'

const UseStateExample = () => {
    const [count , setCount] = useState(0)
  return (
    <div>
      <h1>Counter</h1>
      <p>{count}</p>
      <button onClick={() => setCount(count + 1)}>Click Me</button>
    </div>
  )
}

export default UseStateExample
