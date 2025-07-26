// 1. Code Splitting (Dynamic Imports)

import React, { Suspense, lazy } from 'react';

const LazyComponent = lazy(() => import('./HeavyComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <LazyComponent />
    </Suspense>
  );
}

// 2. Memoization with React.memo or useMemo

const MyComponent = React.memo(({ value }) => {
  console.log('Rendering MyComponent');
  return <div>{value}</div>;
});

// 3. Lazy Load Images

<img src="image.jpg" loading="lazy" alt="..." />
