
import React, { Suspense, lazy } from "react";

const LazyComponent = lazy(() => import("./LazyComponent"));

function App() {
  return (
    <div>
      <h1>Main App</h1>
      
      <Suspense fallback={<p>Loading component...</p>}>
        <LazyComponent />
      </Suspense>
    </div>
  );
}

export default App;
