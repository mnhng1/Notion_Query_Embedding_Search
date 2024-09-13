import {  Outlet } from 'react-router-dom'
import { useAuth } from './AuthContext';

const PrivateRoutes = () => {
    const { isAuthenticated } = useAuth(); 
return (
    isAuthenticated ? <Outlet /> : window.location.href = "http://localhost:8000/oauth/login/"
  )
}


export default PrivateRoutes