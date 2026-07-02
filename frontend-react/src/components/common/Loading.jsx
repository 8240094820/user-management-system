import {
  Box,
  CircularProgress,
  Typography,
} from "@mui/material";

function Loading() {
  return (
    <Box
      sx={{
        height: "60vh",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        gap: 2,
      }}
    >
      <CircularProgress size={60} />

      <Typography variant="h6">
        Loading...
      </Typography>
    </Box>
  );
}

export default Loading;