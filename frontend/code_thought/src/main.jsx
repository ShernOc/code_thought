import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter as Router } from 'react-router'
import './index.css'
import App from './components/App'

ReactDOM.createRoot(document.getElementById('root')).render(

  <React.StrictMode>
    <Router>
    <App />
    </Router>
  </React.StrictMode>
); 
