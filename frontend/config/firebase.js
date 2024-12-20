// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey:"AIzaSyBUWj46dCKPq6gdW0otWsPRJnFGkZpphkI",
  authDomain: "",
  projectId: "code-thouts",
  storageBucket: "book-management-ea099.appspot.com",
  messagingSenderId: "48690010705",
  appId:"1:48690010705:web:087ae27d5ffc01e87c7670"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export const auth = getAuth(app)