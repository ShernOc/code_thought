import { NavLink } from "react-router";

function Navbar() {
    // Array of navbar links 
    // const links = ["Home","About","ShowBlog","Contact"]

    // We are going to return the links, and have the key prop included

    return (
        <nav id = "navbar">
            <p className="font-semibold ">CODE-Thoughts</p>
            <NavLink to = "/">Home</NavLink>
            <NavLink to = "./src/components/About.jsx">About</NavLink>
            <NavLink to ="./src/components/ShowBlog ">Blogs</NavLink>
            <NavLink to = "./src/components/Contact.jsx">Contacts</NavLink>
            </nav>
    )
}

export default Navbar;