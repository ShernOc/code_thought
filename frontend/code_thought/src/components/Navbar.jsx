import { NavLink,} from "react-router";
import { useAuth } from "./Signin";
import { Link } from "react-router";

export const Navbar=() =>{
    // Array of navbar links 
    // const links = ["Home","About","ShowBlog","Contact"]
        const {user, logout} = useAuth(); 
    // We are going to return the links, and have the key prop included

    return (
        <nav id = "navbar" className="flex justify-between w-full">
            <h1 className=" font-fredoka
            text-3xl font-bold">CODE-Thoughts</h1>
            <div className="flex gap-4">
            <NavLink to = "/">Home</NavLink>
            <NavLink to = "blogs">Blogs</NavLink> 
            {user ?(
            <>
            <NavLink to = "/blogcard">Create Blog</NavLink>
            <button onClick={logout} className="hover:underline">Logout</button>
            </>
            ):(
            <Link to="/login" className="hover:underline">Login</Link>
            )}
        </div>     
     </nav>
    );
};

export default Navbar;