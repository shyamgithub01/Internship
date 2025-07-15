function HoverExample() {
  const handleMouseOver = () => {
    console.log("Mouse is over the text!");
  };

  return <h2 onMouseOver={handleMouseOver}>Hover over me</h2>;
}

export default HoverExample