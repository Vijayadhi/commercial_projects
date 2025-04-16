// src/layouts/MainLayout.jsx
import React from 'react';
import {
    AppBar,
    Box,
    CssBaseline,
    Divider,
    Drawer,
    IconButton,
    List,
    ListItem,
    ListItemIcon,
    ListItemText,
    Toolbar,
    Typography
} from '@mui/material';
import {
    Menu as MenuIcon,
    Dashboard as DashboardIcon,
    Logout as LogoutIcon,
    MeetingRoom
} from '@mui/icons-material';
import SensorsIcon from '@mui/icons-material/Sensors';
import LeakRemoveIcon from '@mui/icons-material/LeakRemove';
import { useNavigate } from 'react-router-dom';

const drawerWidth = 240;

function MainLayout({ children, window }) {
    const [mobileOpen, setMobileOpen] = React.useState(false);
    const navigate = useNavigate();

    const handleDrawerToggle = () => {
        setMobileOpen(!mobileOpen);
    };

    const handleLogout = () => {
        localStorage.clear();
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
                { text: 'Buildings', icon: <MeetingRoom />, path: '/buildings' },
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
        <Box sx={{ display: 'flex' }}>
            <CssBaseline />
            <AppBar
                position="fixed"
                sx={{
                    width: { sm: `calc(100% - ${drawerWidth}px)` },
                    ml: { sm: `${drawerWidth}px` },
                    backgroundColor: '#3f51b5'
                }}
            >
                <Toolbar>
                    <IconButton
                        color="inherit"
                        aria-label="open drawer"
                        edge="start"
                        onClick={handleDrawerToggle}
                        sx={{ mr: 2, display: { sm: 'none' } }}
                    >
                        <MenuIcon />
                    </IconButton>
                    <Typography variant="h6" noWrap component="div">
                        Admin Panel
                    </Typography>
                </Toolbar>
            </AppBar>
            <Box
                component="nav"
                sx={{ width: { sm: drawerWidth }, flexShrink: { sm: 0 } }}
                aria-label="mailbox folders"
            >
                <Drawer
                    container={container}
                    variant="temporary"
                    open={mobileOpen}
                    onClose={handleDrawerToggle}
                    ModalProps={{ keepMounted: true }}
                    sx={{
                        display: { xs: 'block', sm: 'none' },
                        '& .MuiDrawer-paper': { boxSizing: 'border-box', width: drawerWidth }
                    }}
                >
                    {drawer}
                </Drawer>
                <Drawer
                    variant="permanent"
                    sx={{
                        display: { xs: 'none', sm: 'block' },
                        '& .MuiDrawer-paper': { boxSizing: 'border-box', width: drawerWidth }
                    }}
                    open
                >
                    {drawer}
                </Drawer>
            </Box>
            <Box
                component="main"
                sx={{ flexGrow: 1, p: 3, width: { sm: `calc(100% - ${drawerWidth}px)` } }}
            >
                <Toolbar />
                {children}
            </Box>
        </Box>
    );
}

export default MainLayout;

// Example usage in pages:
// In Dashboard.jsx:
// import MainLayout from '../layouts/MainLayout';
// const Dashboard = () => (
//   <MainLayout>
//     <Typography paragraph>
//       Welcome to your elegant dashboard! Select items from the menu to continue.
//     </Typography>
//   </MainLayout>
// );
// export default Dashboard;
