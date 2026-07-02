import {
  Box,
  Button,
  Typography,
  TextField,
} from "@mui/material";

function UserToolbar({
  search,
  setSearch,
  setOpen,
}) {
  return (
    <Box mb={3}>
      <Box
        display="flex"
        justifyContent="space-between"
        alignItems="center"
      >
        <Typography variant="h4">
          Users
        </Typography>

        <Button
          variant="contained"
          onClick={() => setOpen(true)}
        >
          Add User
        </Button>
      </Box>

      <TextField
        fullWidth
        label="Search Users"
        margin="normal"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />
    </Box>
  );
}

export default UserToolbar;