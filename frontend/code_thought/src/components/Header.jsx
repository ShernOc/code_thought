import Dashboard from "./Dashboard";
import Navbar from "./Navbar";

function Header() {
    return (
        <>
            <header className="header">
                <p>WHAT IS GOING ON? </p>
                <Navbar />
                <Dashboard />
            </header>

        </>
    )

}

export default Header;