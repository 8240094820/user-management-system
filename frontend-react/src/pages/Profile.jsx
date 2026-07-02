import { useEffect, useState } from "react";

import {
  Avatar,
  Box,
  Button,
  Card,
  CardContent,
  Divider,
  Stack,
  TextField,
  Typography,
} from "@mui/material";

import DashboardLayout from "../layouts/DashboardLayout";
import api from "../api/api";

function Profile() {

  const [user, setUser] = useState({
    name: "",
    email: "",
    role: "",
  });

  useEffect(() => {
    fetchProfile();
  }, []);

  const fetchProfile = async () => {
    try {

      const response = await api.get("/profile");

      setUser(response.data.data);

    } catch (error) {
      console.error(error);
    }
  };

  return (

    <DashboardLayout>

      <Typography
        variant="h4"
        mb={3}
      >
        My Profile
      </Typography>

      <Card>

        <CardContent>

          <Stack
            spacing={3}
            alignItems="center"
          >

            <Avatar
              sx={{
                width: 120,
                height: 120,
                fontSize: 50,
              }}
            >
              {user.name?.charAt(0)}
            </Avatar>

            <Divider flexItem />

            <Box
              width="100%"
            >

              <TextField
                label="Name"
                value={user.name}
                fullWidth
                margin="normal"
                disabled
              />

              <TextField
                label="Email"
                value={user.email}
                fullWidth
                margin="normal"
                disabled
              />

              <TextField
                label="Role"
                value={user.role}
                fullWidth
                margin="normal"
                disabled
              />

            </Box>

            <Button
              variant="contained"
            >
              Change Password
            </Button>

          </Stack>

        </CardContent>

      </Card>

    </DashboardLayout>

  );

}

export default Profile;