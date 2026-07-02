import { useContext } from "react";
import { Outlet, Link, useNavigate } from "react-router-dom";

import {
  AppBar,
  Toolbar,
  Typography,
  Box,
  Drawer,
  List,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  IconButton,
  Button,
} from "@mui/material";

import DashboardIcon from "@mui/icons-material/Dashboard";
import PeopleIcon from "@mui/icons-material/People";
import PersonIcon from "@mui/icons-material/Person";
import LightModeIcon from "@mui/icons-material/LightMode";
import DarkModeIcon from "@mui/icons-material/DarkMode";

import { ThemeContext } from "../contexts/ThemeContext";

const drawerWidth = 240;

function DashboardLayout({ children }) {
  const navigate = useNavigate();

  const { darkMode, toggleTheme } =
    useContext(ThemeContext);

  const logout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  return (
    <Box sx={{ display: "flex" }}>
      <AppBar
        position="fixed"
        sx={{
          zIndex: 1201,
        }}
      >
        <Toolbar>
          <Typography
            variant="h6"
            sx={{
              flexGrow: 1,
            }}
          >
            User Management System
          </Typography>

          <IconButton
            color="inherit"
            onClick={toggleTheme}
          >
            {darkMode ? (
              <LightModeIcon />
            ) : (
              <DarkModeIcon />
            )}
          </IconButton>

          <Button
            color="inherit"
            onClick={logout}
          >
            Logout
          </Button>
        </Toolbar>
      </AppBar>

      <Drawer
        variant="permanent"
        sx={{
          width: drawerWidth,
          flexShrink: 0,
          "& .MuiDrawer-paper": {
            width: drawerWidth,
            boxSizing: "border-box",
            mt: "64px",
          },
        }}
      >
        <List>
          <ListItemButton
            component={Link}
            to="/dashboard"
          >
            <ListItemIcon>
              <DashboardIcon />
            </ListItemIcon>

            <ListItemText primary="Dashboard" />
          </ListItemButton>

          <ListItemButton
            component={Link}
            to="/users"
          >
            <ListItemIcon>
              <PeopleIcon />
            </ListItemIcon>

            <ListItemText primary="Users" />
          </ListItemButton>

          <ListItemButton
            component={Link}
            to="/profile"
          >
            <ListItemIcon>
              <PersonIcon />
            </ListItemIcon>

            <ListItemText primary="Profile" />
          </ListItemButton>
        </List>
      </Drawer>

      <Box
        component="main"
        sx={{
          flexGrow: 1,
          p: 4,
          mt: "64px",
          ml: `${drawerWidth}px`,
        }}
      >
        {children || <Outlet />}
      </Box>
    </Box>
  );
}

export default DashboardLayout;