import { useState } from 'react';
import ChildA from './ChildA';
import ChildB from './ChildB';

function Parent() {
  const [text, setText] = useState('');

  return (
    <div>
      <ChildA setText={setText} />
      <ChildB text={text} />
    </div>
  );
}