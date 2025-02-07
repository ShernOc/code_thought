import{ useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
// import Blogcard from './Blogcard';

function Blog(){
    //useState/UseEffect to create blog
    const [blogs, setBlogs] = useState([]);
    const [loading,setLoading] = useState(true);
    
    useEffect(() => {
        axios.get('/api/blog').then((response) => {
          setBlogs(response.data);
          setLoading(false);
    })
        
        })
          .catch((error) => {
            console.error('Error fetching blogs:', error);
            setLoading(false);
      
      }, 
      []);
      if (loading) {
        return <div>Loading...</div>;
      }
      
    return(
        <>
        {/* Want when a button is clicked a user writes presses the blog a blog */}

        <div className="container mx-auto p-4" id='blog'>
      <h2 className="text-xl font-bold mb-4">The Blogs</h2>
      {blogs.map((blog) => (
        <div key={blog.id} className="border p-4 mb-4 rounded shadow">
          <h3 className="text-lg font-semibold">{blog.title}</h3>
          <p>{blog.content.substring(0, 100)}...</p>
        {/* Directs you to a link for blogs */}
          <Link to={`/blogcard/${blog.id}`} className="text-blue-500">Read More</Link>
        </div>
      ))}
    </div>
    </>
    );
};

export default Blog;