
import './App.css'
// import {Routes,Route } from 'react-router'
import Contact from './Contact'
import  Dashboard from './Dashboard'
import ShowBlog from './ShowBlog'
import Footer from './Footer'
import Signin from './Signin'
import Signout from './Signout'
import About from './About'


function App() {
  return (
    <> 
    <Dashboard/>
    <About/>
    <ShowBlog/>
    <Contact/>
    <Footer/>
    <Signin/>
    <Signout/>

     {/* <Routes>
      <Route path='/dashboard' element = { <Dashboard/>}/>
      <Route path='/about' element = { <About/>}/>
      <Route path='/show-blog' element = { <ShowBlog/>}/>
      <Route path='/contact' element = { <Contact/>}/>
      <Route path='/footer' element = { <Footer/>}/>
      <Route path='/signin' element = { <Signin/>}/>
      <Route path='/signout' element = { <Signout/>}/>
    </Routes>  */}

{/*    
    <ShowBlog/>
    <Contact />
    <Footer/> */}
    </>
  );
};

export default App