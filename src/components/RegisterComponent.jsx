import React, { useState } from 'react';
import { Container, TextField, Button, Typography, Box } from '@mui/material';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useNavigate } from 'react-router-dom';

const RegisterComponent = () => {
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleRegister = () => {
    if (email && password && username) {
      navigate('/');
    }
  };

  return (
    <Container maxWidth="sm" className="mt-5 shadow p-4 bg-white rounded">
      <Typography variant="h4" align="center" gutterBottom>
        Register
      </Typography>
      <TextField
        label="Username"
        fullWidth
        margin="normal"
        variant="outlined"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
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
        <Button variant="contained" color="primary" onClick={handleRegister}>
          Register
        </Button>
      </Box>
      <Box textAlign="center" mt={2}>
        <Button variant="text" onClick={() => navigate('/')}>
          Already have an account? Login
        </Button>
      </Box>
    </Container>
  );
};

export default RegisterComponent;
