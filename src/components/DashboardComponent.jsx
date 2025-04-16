// src/pages/Dashboard.jsx
import React from 'react';
import { AppBar, Box, CssBaseline, Divider, Drawer, IconButton, List, ListItem, ListItemIcon, ListItemText, Toolbar, Typography } from '@mui/material';
import { Menu as MenuIcon, Dashboard as DashboardIcon, Assignment as AssignmentIcon, Logout as LogoutIcon, MeetingRoom } from '@mui/icons-material';
import SensorsIcon from '@mui/icons-material/Sensors';
import { useNavigate } from 'react-router-dom';
import LeakRemoveIcon from '@mui/icons-material/LeakRemove';
import MainLayout from './MainLayout';

const drawerWidth = 240;

function DashboardComponent(props) {
    const { window } = props;
    const [mobileOpen, setMobileOpen] = React.useState(false);
    const navigate = useNavigate();

    const handleDrawerToggle = () => {
        setMobileOpen(!mobileOpen);
    };

    const handleLogout = () => {
        localStorage.removeItem('access'); // Clear any auth tokens or user data
        navigate('/');
    };

    const drawer = (
        <div>
            <Toolbar>
                <Typography variant="h6" noWrap>
                    Admin Panel
                </Typography>
            </Toolbar>
            <Divider />
            <List>
                {[{ text: 'Dashboard', icon: <DashboardIcon />, path: '/dashboard' },
                { text: 'Buildings', icon: <MeetingRoom />, path: '/builldings' },
                { text: 'Sensors', icon: <SensorsIcon />, path: '/sensors' },
                { text: 'Dilutions', icon: <LeakRemoveIcon />, path: '/dilutions' }].map((item) => (
                    <ListItem button key={item.text} onClick={() => navigate(item.path)}>
                        <ListItemIcon>{item.icon}</ListItemIcon>
                        <ListItemText primary={item.text} />
                    </ListItem>
                ))}
                <ListItem button key="Logout" onClick={handleLogout}>
                    <ListItemIcon><LogoutIcon /></ListItemIcon>
                    <ListItemText primary="Logout" />
                </ListItem>
            </List>
        </div>
    );

    const container = window !== undefined ? () => window().document.body : undefined;

    return (
        <MainLayout>
            {/* <Box
                component="main"
                sx={{ flexGrow: 1, p: 3, width: { sm: `calc(100% - ${drawerWidth}px)` } }}
            > */}
            <Toolbar />
            <Typography paragraph>
                Welcome to your elegant dashboard! Select items from the menu to continue.
            </Typography>
            {/* </Box> */}
        </MainLayout>
    );
}

export default DashboardComponent;
