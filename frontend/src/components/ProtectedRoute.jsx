// ProtectedRoute.jsx
import { Outlet, Navigate } from 'react-router-dom';
import { useAuth } from './AuthContext';

const ProtectedRoute = () => {
  const { isAuthenticated, loading } = useAuth();

  if (loading) {
    return <p>Loading...</p>; // Show a loading state while checking authentication
  }
  
  return isAuthenticated ? <Outlet /> : window.location.href =  "http://localhost:8000/oauth/login" ;
};

export default ProtectedRoute;