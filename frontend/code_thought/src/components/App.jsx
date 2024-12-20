import './App.css'
import {Routes,Route } from 'react-router-dom';
import Contact from './Contact';
import Home from './Home';
import About from './About';
import Blog from './Blog';
import Footer from './Footer';
import Login from './Login';
import {Navbar} from './Navbar'
import { AuthProvider} from './Signin' ;


function App() {
  return (
    <>
    <AuthProvider>
    <div className='container' >
      <Navbar/>
      <Routes>
      <Route path='/' element = { <Home/>}/>
      <Route path='/about' element = { <About/>}/>
      <Route path='/contact' element = { <Contact/>}/>
      <Route path='/blog' element = { <Blog/>}/>
      <Route path='/login' element = { <Login/>}/>
    </Routes> 
    </div>
    <Footer/>
    </AuthProvider>
    </>
  );
};
export default App;