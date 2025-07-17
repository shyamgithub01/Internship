
import MyButton from './components/MyButton';

function App() {
  const sayHello = () => alert("Hello!");
  const sayBye = () => alert("Bye!");

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">Reusable Button Example</h1>

      {/* Using same button with different text and actions */}
      <MyButton text="Say Hello" onClick={sayHello} />
      <br /><br />
      <MyButton text="Say Bye" onClick={sayBye} />
    </div>
  );
}

export default App;
