import React, { useState } from 'react';
import { Container, TextField, Button, Typography, Box, Paper } from '@mui/material';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const LoginComponent = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleLogin = async (e) => {
        e.preventDefault();

        if (!email || !password) {
            alert('Please fill in all fields');
            return;
        }
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/auth/token/login/', {
                email,
                password
            });
            if (response.status === 200) {
                localStorage.setItem('access', response.data.auth_token	); // Assuming the token is returned in the response
                navigate('/dashboard') // Redirect to dashboard or home page
            }
            console.log(response.data);

        }
        catch (error) {
            console.error('Error logging in:', error);
            alert('Login failed. Please check your credentials.');
        }
    };

    return (
        <div className="bg-info-subtle min-vh-100 d-flex align-items-center justify-content-center">
            <Container maxWidth="sm">
                <Paper elevation={5} sx={{ padding: 4, borderRadius: 3, background: '#e3f2fd' }}>
                    <Typography variant="h4" align="center" gutterBottom color="primary">
                        Login
                    </Typography>
                    <TextField
                        label="Email"
                        fullWidth
                        margin="normal"
                        variant="outlined"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                    />
                    <TextField
                        label="Password"
                        fullWidth
                        margin="normal"
                        type="password"
                        variant="outlined"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                    <Box textAlign="center" mt={2}>
                        <Button variant="contained" color="primary" onClick={handleLogin}>
                            Login
                        </Button>
                    </Box>
                    <Box textAlign="center" mt={2}>
                        <Button variant="text" onClick={() => navigate('/register')}>
                            Don't have an account? Register
                        </Button>
                    </Box>
                </Paper>
            </Container>
        </div>
    );
};

export default LoginComponent;
