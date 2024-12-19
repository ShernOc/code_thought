import {useState, useEffect } from 'react';

function HomePage({data}){
    
    const [blogs, setBlogs] = useState([]);
    const [filteredBlogs, setFilteredBlogs] = useState([])
    const [searchKey, setSearchKey] = useState('');
    // Search submit
    const handleSearchBar = (e) => {
      e.preventDefault();
      handleSearchResults();
    };
    // Search for blog by category
    const handleSearchResults = () => {
     //handle search inputs
    };
    // Clear search and show all blogs
    const handleClearSearch = () => {
      blogList().then((res) => {
        setBlogs(res);
      })
      setSearchKey("");
    };
  
    // function to get selected blog content
   const BlogContent = (id) => {
    data(id);
  }
    return (
      <div>
        {/* Page Header */}
        <Header />
        {/* Search Bar */}
        <SearchBar
          value={searchKey}
          clearSearch={handleClearSearch}
          formSubmit={handleSearchBar}
          handleSearchKey={(e) => setSearchKey(e.target.value)}
        />
        {/* Blog List & Empty View */}
        {!filteredBlogs.length ? <EmptyList /> : <BlogList blogs={filteredBlogs} content = {BlogContent}/>}
      </div>
    );
  };
  export default HomePage;