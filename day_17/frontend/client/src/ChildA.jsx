function ChildA({ setText }) {
  return (
    <input
      type="text"
      onChange={(e) => setText(e.target.value)}
      placeholder="Type something"
    />
  );
}
