import { useEffect, useState } from "react";

import {
  Grid,
  Typography,
} from "@mui/material";

import PeopleAltIcon from "@mui/icons-material/PeopleAlt";
import AdminPanelSettingsIcon from "@mui/icons-material/AdminPanelSettings";
import BadgeIcon from "@mui/icons-material/Badge";

import DashboardLayout from "../layouts/DashboardLayout";

import StatCard from "../components/dashboard/StatCard";
import DashboardChart from "../components/dashboard/DashboardChart";
import RecentUsers from "../components/dashboard/RecentUsers";

import api from "../api/api";

function Dashboard() {

  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {

      const response = await api.get("/users");

      setUsers(response.data.data);

    } catch (error) {

      console.error(error);

    }
  };

  const totalUsers = users.length;

  const adminUsers = users.filter(
    (user) => user.role === "Admin"
  ).length;

  const staffUsers = users.filter(
    (user) => user.role === "Staff"
  ).length;

  return (

    <DashboardLayout>

      <Typography
        variant="h4"
        sx={{
          mb: 4,
          fontWeight: 700,
        }}
      >
        Dashboard
      </Typography>

      <Grid
        container
        spacing={3}
      >

        <Grid
          item
          xs={12}
          md={4}
        >

          <StatCard
            title="Total Users"
            value={totalUsers}
            color="linear-gradient(135deg,#2563EB,#3B82F6)"
            icon={<PeopleAltIcon sx={{ fontSize: 60 }} />}
          />

        </Grid>

        <Grid
          item
          xs={12}
          md={4}
        >

          <StatCard
            title="Admin Users"
            value={adminUsers}
            color="linear-gradient(135deg,#7C3AED,#9333EA)"
            icon={<AdminPanelSettingsIcon sx={{ fontSize: 60 }} />}
          />

        </Grid>

        <Grid
          item
          xs={12}
          md={4}
        >

          <StatCard
            title="Staff Users"
            value={staffUsers}
            color="linear-gradient(135deg,#16A34A,#22C55E)"
            icon={<BadgeIcon sx={{ fontSize: 60 }} />}
          />

        </Grid>

        <Grid
          item
          xs={12}
          md={7}
        >

          <DashboardChart
            admin={adminUsers}
            staff={staffUsers}
          />

        </Grid>

        <Grid
          item
          xs={12}
          md={5}
        >

          <RecentUsers
            users={users}
          />

        </Grid>

      </Grid>

    </DashboardLayout>

  );
}

export default Dashboard;