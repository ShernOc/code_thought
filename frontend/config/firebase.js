// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyBUWj46dCKPq6gdW0otWsPRJnFGkZpphkI",
    authDomain: "code-thouts.firebaseapp.com",
    projectId: "code-thouts",
    storageBucket: "code-thouts.firebasestorage.app",
    messagingSenderId: "243001299356",
    appId: "1:243001299356:web:593be73d7dee5c91da7859",
    measurementId: "G-1FDK9RWSVZ"
  };

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth= getAuth(app);

export { auth };


