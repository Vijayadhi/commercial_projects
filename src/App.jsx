import React from 'react'
import { BrowserRouter, createBrowserRouter, Route, RouterProvider, Routes } from 'react-router-dom'
import AppRoutes from './routes/AppRoutes'
function App() {
  const router = createBrowserRouter(AppRoutes)

  return (
    <>
      <RouterProvider router={router} />

    </>
  )
}

export default App