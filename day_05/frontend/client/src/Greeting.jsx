// function Greeting({ isLoggedIn }) {
//   if (!isLoggedIn) {
//     return <h2>Welcome Back!</h2>;
//   } else {
//     return <h2>Please Sign In</h2>;
//   }
// }

function Greeting({ isLoggedIn }) {
  return (
    <h2>{isLoggedIn ? "Welcome Back!" : "Please Sign In"}</h2>
  );
}


export default Greeting