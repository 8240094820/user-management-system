import { useState, useEffect } from "react";

import { useSnackbar } from "notistack";

import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  TextField,
  MenuItem,
  Stack,
} from "@mui/material";

import api from "../../api/api";

function UserDialog({
  open,
  setOpen,
  fetchUsers,
  selectedUser,
  setSelectedUser,
}) {

  const { enqueueSnackbar } = useSnackbar();

  const [name, setName] = useState("");

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");

  const [role, setRole] = useState("Staff");

  useEffect(() => {

    if (selectedUser) {

      setName(selectedUser.name);

      setEmail(selectedUser.email);

      setRole(selectedUser.role);

      setPassword("");

    } else {

      setName("");

      setEmail("");

      setPassword("");

      setRole("Staff");

    }

  }, [selectedUser]);

  const handleClose = () => {

    setOpen(false);

    setSelectedUser(null);

    setName("");

    setEmail("");

    setPassword("");

    setRole("Staff");

  };

  const handleSave = async () => {

    try {

      if (selectedUser) {

        const payload = {
          name,
          email,
          role,
        };

        if (password.trim() !== "") {
          payload.password = password;
        }

        await api.patch(
          `/users/${selectedUser.id}`,
          payload
        );

        enqueueSnackbar(
          "User Updated Successfully",
          {
            variant: "success",
          }
        );

      } else {

        await api.post("/users", {
          name,
          email,
          password,
          role,
        });

        enqueueSnackbar(
          "User Created Successfully",
          {
            variant: "success",
          }
        );

      }

      fetchUsers();

      handleClose();

    } catch (error) {

      enqueueSnackbar(
        "Operation Failed",
        {
          variant: "error",
        }
      );

      console.error(error);

    }

  };

  return (
    <Dialog
      open={open}
      onClose={handleClose}
      fullWidth
      maxWidth="sm"
    >
      <DialogTitle>
        {selectedUser ? "Edit User" : "Add User"}
      </DialogTitle>

      <DialogContent>

        <Stack
          spacing={2}
          sx={{ mt: 1 }}
        >

          <TextField
            label="Name"
            value={name}
            fullWidth
            onChange={(e) =>
              setName(e.target.value)
            }
          />

          <TextField
            label="Email"
            value={email}
            fullWidth
            onChange={(e) =>
              setEmail(e.target.value)
            }
          />

          <TextField
            label={
              selectedUser
                ? "Password (Optional)"
                : "Password"
            }
            type="password"
            value={password}
            fullWidth
            onChange={(e) =>
              setPassword(e.target.value)
            }
          />

          <TextField
            select
            label="Role"
            value={role}
            fullWidth
            onChange={(e) =>
              setRole(e.target.value)
            }
          >
            <MenuItem value="Admin">
              Admin
            </MenuItem>

            <MenuItem value="Staff">
              Staff
            </MenuItem>

          </TextField>

        </Stack>

      </DialogContent>

      <DialogActions>

        <Button
          onClick={handleClose}
        >
          Cancel
        </Button>

        <Button
          variant="contained"
          onClick={handleSave}
        >
          {selectedUser ? "Update" : "Save"}
        </Button>

      </DialogActions>

    </Dialog>
  );
}

export default UserDialog;