import {
  DataGrid,
} from "@mui/x-data-grid";

import {
  Paper,
  Chip,
  IconButton,
  Stack,
} from "@mui/material";

import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";

function UserTable({
  users,
  handleDelete,
  handleEdit,
}) {

  const columns = [

    {
      field: "id",
      headerName: "ID",
      width: 80,
    },

    {
      field: "name",
      headerName: "Name",
      flex: 1,
    },

    {
      field: "email",
      headerName: "Email",
      flex: 1.5,
    },

    {
      field: "role",
      headerName: "Role",
      width: 150,

      renderCell: (params) => (

        <Chip
          label={params.value}
          color={
            params.value === "Admin"
              ? "primary"
              : "success"
          }
        />

      ),
    },

    {
      field: "actions",

      headerName: "Actions",

      width: 150,

      sortable: false,

      renderCell: (params) => (

        <Stack
          direction="row"
        >

          <IconButton
            color="primary"
            onClick={() =>
              handleEdit(params.row)
            }
          >

            <EditIcon />

          </IconButton>

          <IconButton
            color="error"
            onClick={() =>
              handleDelete(params.row.id)
            }
          >

            <DeleteIcon />

          </IconButton>

        </Stack>

      ),
    },

  ];

  return (

    <Paper
      sx={{
        height: 550,
        mt: 3,
      }}
    >

      <DataGrid

        rows={users}

        columns={columns}

        pageSizeOptions={[
          5,
          10,
          20,
        ]}

        initialState={{
          pagination: {
            paginationModel: {
              pageSize: 5,
            },
          },
        }}

      />

    </Paper>

  );

}

export default UserTable;