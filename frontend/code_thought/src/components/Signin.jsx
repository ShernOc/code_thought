import { createContext, useContext, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import firebase from 'firebase/compat/app';


// Authentication 
const Signin = createContext();

export const AuthProvider = ({children})=>{
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  const login = async (email, password) => {
    try {
      const { user } = await firebase.auth().signInWithEmailAndPassword(email, password);
      setUser(user);
      navigate('./blogs');
    } catch (error) {
      console.error(error);
    }
  };

  const logout = async () => {
    await firebase.auth().signOut();
    setUser(null);
    navigate('/');
  };

  return (
    <Signin.Provider value={{ user, login, logout }}>
      {children}
    </Signin.Provider>
  );
};

export const useAuth = () => useContext(Signin);