import { Button, Container, Typography } from "@mui/material";
import { useNavigate } from "react-router-dom";

function NotFound() {
  const navigate = useNavigate();

  return (
    <Container
      maxWidth="sm"
      sx={{
        height: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <div style={{ textAlign: "center" }}>
        <Typography variant="h1" fontWeight="bold">
          404
        </Typography>

        <Typography
          variant="h5"
          sx={{ mb: 3 }}
        >
          Page Not Found
        </Typography>

        <Button
          variant="contained"
          onClick={() => navigate("/dashboard")}
        >
          Back To Dashboard
        </Button>
      </div>
    </Container>
  );
}

export default NotFound;