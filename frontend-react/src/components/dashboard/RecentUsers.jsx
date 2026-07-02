import {
  Card,
  CardContent,
  Typography,
  Avatar,
  Stack,
  Divider,
} from "@mui/material";

function RecentUsers({
  users,
}) {
  return (
    <Card>

      <CardContent>

        <Typography
          variant="h6"
          mb={2}
        >
          Recent Users
        </Typography>

        <Stack spacing={2}>

          {users.slice(0, 5).map((user) => (

            <div key={user.id}>

              <Stack
                direction="row"
                spacing={2}
                alignItems="center"
              >

                <Avatar>
                  {user.name[0]}
                </Avatar>

                <div>

                  <Typography
                    fontWeight="bold"
                  >
                    {user.name}
                  </Typography>

                  <Typography
                    color="text.secondary"
                    variant="body2"
                  >
                    {user.email}
                  </Typography>

                </div>

              </Stack>

              <Divider sx={{ mt: 2 }} />

            </div>

          ))}

        </Stack>

      </CardContent>

    </Card>
  );
}

export default RecentUsers;