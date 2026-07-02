import {
  Card,
  CardContent,
  Typography,
  Box,
} from "@mui/material";

function StatCard({
  title,
  value,
  icon,
  color,
}) {
  return (
    <Card
      sx={{
        background: color,
        color: "#fff",
        height: 170,
        borderRadius: 4,
      }}
    >
      <CardContent>

        <Box
          display="flex"
          justifyContent="space-between"
          alignItems="center"
        >

          <Box>

            <Typography
              variant="h6"
            >
              {title}
            </Typography>

            <Typography
              variant="h3"
              fontWeight="bold"
              mt={2}
            >
              {value}
            </Typography>

          </Box>

          <Box
            sx={{
              fontSize: 60,
            }}
          >
            {icon}
          </Box>

        </Box>

      </CardContent>
    </Card>
  );
}

export default StatCard;