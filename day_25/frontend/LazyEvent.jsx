import React, { Suspense, lazy, useState } from "react";

const LazyComponent = lazy(() => import("./LazyComponent"));

export default function App() {
  const [show, setShow] = useState(false);

  return (
    <div>
      <h1>Hello!</h1>
      <button onClick={() => setShow(true)}>Load Component</button>

      {show && (
        <Suspense fallback={<p>Loading...</p>}>
          <LazyComponent />
        </Suspense>
      )}
    </div>
  );
}
