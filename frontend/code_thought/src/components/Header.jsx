import Dashboard from "./Dashboard";
import Navbar from "./Navbar";


function Header() {
    return (
        <>
            <header className="header">
                <h2>Code-Thoughts</h2>
                <h1>
                    <span></span>
                </h1>
                <Navbar/>
                <Dashboard />
            </header>

        </>
    )

}

export default Header;