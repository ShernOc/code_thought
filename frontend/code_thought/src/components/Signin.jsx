/* eslint-disable react/prop-types */
import { createContext, useContext, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { signInWithEmailAndPassword,signOut } from 'firebase/auth'
import { auth } from '../../../config/firebase';

// Authentication 
const Signin = createContext();

export const AuthProvider = ({children})=>{
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  const login = async (email, password) => {
    try {
      const userCredential = await signInWithEmailAndPassword(auth,email, password);
      setUser(userCredential.user);
      navigate('/blogs');
    } catch (error) {
      console.error(error);
    }
  };

  const logout = async () => {
    await signOut(auth);
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