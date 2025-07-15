import { Outlet , Link } from "react-router-dom"

function About(){
       return (
        <>
            <h1> About page</h1>
            <nav>
            <Link to='/team'></Link>
            <Link to = 'goal'></Link>

        </nav>
        <Outlet/>
        </>
       )
}

export default About