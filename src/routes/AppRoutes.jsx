// import BuildingsComponent from "../components/BuildingsComponent";
// import ContentWrapper from "../components/ContentWrapper";
// import DashboardComponent from "../components/DashboardComponent";
// import ClientTools from "../components/ClientTools";
import { Settings } from "lucide-react";
import DashboardComponent from "../components/DashboardComponent";
// import GoogleCallback from "../components/GoogleCallback";
// import HomePage from "../components/HomePage";
// import IPComponent from "../components/IPComponent";
import HomePageComponent from "../components/HomePageComponent";
import LoginComponent from "../components/LoginComponent";
// import ProfileComponent from "../components/ProfileComponent";
import RegisterComponent from "../components/RegisterComponent";
// import SitesComponent from "../components/SitesComponent";
// import UsersComponent from "../components/UsersComponent";
// import ProfileComponent from "../components/ProfileComponent";
// import BillComponent from "../components/BillComponent";
// import ContactUs from "../components/ContactUs";
import ProtectedRoute from "./ProtectedRoute"; // Import the ProtectedRoute component
import BuildingsComponent from "../components/BuildingsComponent";
import SensorComponent from "../components/SensorComponent";
import DilutionComponent from "../components/DilutionComponent";
// import SettingsComponent from "../components/SettingsComponent";
// import TryPrototype from "../components/TryPrototype";

export default [
    {
        path: '/register',
        element: (<ProtectedRoute>
            <RegisterComponent />
        </ProtectedRoute>)
    },
    {
        path: '/',
        element: (
            <ProtectedRoute>
                <HomePageComponent />
            </ProtectedRoute>
        )
    },
    {
        path: '/dashboard',
        element: (
            <ProtectedRoute>
                <DashboardComponent />
            </ProtectedRoute>
        )
    },
    {
        path: '/buildings',
        element: (
            <ProtectedRoute>
                <BuildingsComponent/>
            </ProtectedRoute>
        )
    },
    {
        path: '/sensors',
        element: (
            <ProtectedRoute>
                <SensorComponent/>
            </ProtectedRoute>
        )
    },
    {
        path: '/dilutions',
        element: (
            <ProtectedRoute>
                <DilutionComponent/>
            </ProtectedRoute>
        )
    },
    {
        path: '/login',
        element: (<ProtectedRoute>
            <LoginComponent />
        </ProtectedRoute>)
    },
    // {
    //     path: '/google-callback',
    //     element: <GoogleCallback />
    // },
    // {
    //     path: '/profile',
    //     element: (
    //         <ProtectedRoute>
    //             <ProfileComponent />
    //         </ProtectedRoute>
    //     )
    // },
    // {
    //     path: 'settings',
    //     element: (
    //         <ProtectedRoute>
    //             <SettingsComponent />
    //         </ProtectedRoute>
    //     )
    // },
    // {
    //     path: 'prototype',
    //     element: (
    //         <ProtectedRoute>
    //             <TryPrototype/>
    //         </ProtectedRoute>
    //     )
    // }
    // {
    //     path: '/users',
    //     element: (
    //         <ProtectedRoute>
    //             <UsersComponent/>
    //         </ProtectedRoute>
    //     )
    // },
    // {
    //     path: '/sites',
    //     element: (
    //         <ProtectedRoute>
    //             <SitesComponent/>
    //         </ProtectedRoute>
    //     )
    // },
    // {
    //     path: '/ip_table',
    //     element: (
    //         <ProtectedRoute>
    //             <IPComponent/>
    //         </ProtectedRoute>
    //     )
    // },
    // {
    //     path: '/client_tools',
    //     element: (
    //         <ProtectedRoute>
    //             <ClientTools/>
    //         </ProtectedRoute>
    //     )
    // },
    // {
    //     path: '/buildings',
    //     element: (
    //         <ProtectedRoute>
    //             <BuildingsComponent />
    //         </ProtectedRoute>
    //     )
    // },
    // {
    //     path: '/profile',
    //     element: (
    //         <ProtectedRoute>
    //             <ProfileComponent />
    //         </ProtectedRoute>
    //     )
    // },
    // {
    //     path: '/bills',
    //     element: (
    //         <ProtectedRoute>
    //             <BillComponent />
    //         </ProtectedRoute>
    //     )
    // },
    // {
    //     path: '/contact_us',
    //     element: <ContactUs/>
    // }
];