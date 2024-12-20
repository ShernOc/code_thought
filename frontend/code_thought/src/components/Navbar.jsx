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
            <Link to = "/">Home</Link> 
            <Link to = "/About">About</Link> 
            <Link to = "/blogs">Blogs</Link> 
            <Link to = "./contact">Contacts</Link> 
            {user ?(
            <>
            <Link to = "/blogcard/">Create Blog</Link>
            <button onClick={logout} className="bg-green-100
        px-2 py-1 rounded hover:underline">Logout</button>
            </>
            ):(
            <Link to="/login" className="bg-green-100
        px-2 py-1 rounded hover:underline">Login</Link>
            )}
        </div>     
     </nav>
    );
};

export default Navbar;