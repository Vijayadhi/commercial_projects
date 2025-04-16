import React from 'react';
import { Navigate, useLocation } from 'react-router-dom';

const ProtectedRoute = ({ children }) => {
    const authToken = localStorage.getItem('access');
    const location = useLocation();
    const restrictedPaths = ['/login', '/register'];

    // If authToken exists and the current path is login or register, redirect to home/dashboard
    if (authToken && restrictedPaths.includes(location.pathname)) {
        return <Navigate to="/" replace />;
    }
    else if (!authToken && !restrictedPaths.includes(location.pathname)) {
        // If no authToken and the current path is not login or register, redirect to login
        return <Navigate to="/login" state={{ from: location }} replace />;
    }

    // Otherwise, render the requested component
    return children;
};

export default ProtectedRoute;
