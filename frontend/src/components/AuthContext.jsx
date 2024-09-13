// AuthContext.jsx

import React, { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);

  const login = async () => {
    window.location.href = 'http://localhost:8000/oauth/login';
  };

  const logout = async () => {
    // Perform logout logic
    setIsAuthenticated(false);
  };

  const checkAuth = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/is_authenticated/', {
        method: 'GET',
        credentials: 'include',
      });
      const data = await response.json();
      console.log(data)
      if (data.isAuthenticated == true) {
        setIsAuthenticated(true)
      }
      
    } catch (error) {
      console.error('Failed to check authentication:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    checkAuth();
  }, []);

  useEffect(() => {
    console.log('AuthContext isAuthenticated:', isAuthenticated);
  }, [isAuthenticated]);

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout, checkAuth, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);