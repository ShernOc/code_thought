import React from 'react'
import { BrowserRouter } from 'react-router-dom'

import './index.css'
import App from './components/App'

React.createRoot(document.getElementById('root')).render(

  <React.StrictMode>
    <BrowserRouter> 
    <App />
    </BrowserRouter>
  </React.StrictMode>


)
