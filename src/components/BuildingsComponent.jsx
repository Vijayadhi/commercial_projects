// src/pages/BuildingsComponent.jsx
import React, { useEffect, useState } from 'react';
import { Box, Button, Grid, Paper, TextField, Typography } from '@mui/material';
import { DataGrid } from '@mui/x-data-grid';
import MainLayout from './MainLayout';
import axios from 'axios';

function BuildingsComponent() {
    const [formData, setFormData] = useState({
        name: '',
        location: '',
        address: ''
    });
    const [buildings, setBuildings] = useState([]);

    useEffect(() => {
        fetchBuildings();
    }, []);

    const fetchBuildings = async () => {
        try {
            const res = await axios.get('http://127.0.0.1:8000/api/buildings/');
            setBuildings(res.data);
        } catch (err) {
            console.error('Failed to fetch buildings', err);
        }
    };

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
    e.preventDefault();
    try {
        await axios.post(
            'http://127.0.0.1:8000/api/buildings/',
            formData, // first: data
            {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${localStorage.getItem('access')}` // or your preferred auth mechanism
                }
            }
        );
        setFormData({ name: '', location: '', address: '' });
        fetchBuildings();
    } catch (err) {
        console.error('Failed to add building', err);
    }
};


    const columns = [
        { field: 'name', headerName: 'Name', flex: 1 },
        { field: 'location', headerName: 'Location', flex: 1 },
        { field: 'address', headerName: 'Address', flex: 2 }
    ];

    return (
        <MainLayout>
            <Typography variant="h5" gutterBottom>
                Manage Buildings
            </Typography>
            <Grid container spacing={3}>
                <Grid item xs={12} md={4}>
                    <Paper sx={{ p: 2 }}>
                        <form onSubmit={handleSubmit}>
                            <TextField
                                fullWidth
                                label="Building Name"
                                name="name"
                                value={formData.name}
                                onChange={handleChange}
                                margin="normal"
                            />
                            <TextField
                                fullWidth
                                label="Location"
                                name="location"
                                value={formData.location}
                                onChange={handleChange}
                                margin="normal"
                            />
                            <TextField
                                fullWidth
                                label="Address"
                                name="address"
                                value={formData.address}
                                onChange={handleChange}
                                margin="normal"
                                multiline
                                rows={3}
                            />
                            <Button type="submit" variant="contained" color="primary" sx={{ mt: 2 }}>
                                Add Building
                            </Button>
                        </form>
                    </Paper>
                </Grid>
                <Grid item xs={12} md={8}>
                    <Paper sx={{ height: 400, p: 2 }}>
                        <DataGrid
                            rows={buildings}
                            columns={columns}
                            pageSize={5}
                            rowsPerPageOptions={[5, 10]}
                            getRowId={(row) => row.id}
                            sx={{
                                '& .MuiDataGrid-columnHeaders': {
                                    backgroundColor: '#3f51b5',
                                    color: '#fff'
                                }
                            }}
                        />
                    </Paper>
                </Grid>
            </Grid>
        </MainLayout>
    );
}

export default BuildingsComponent;
