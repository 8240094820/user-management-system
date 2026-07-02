import { useEffect, useState } from "react";

import { useSnackbar } from "notistack";

import DashboardLayout from "../layouts/DashboardLayout";

import UserToolbar from "../components/users/UserToolbar";
import UserTable from "../components/users/UserTable";
import UserDialog from "../components/users/UserDialog";

import ConfirmDialog from "../components/common/ConfirmDialog";
import Loading from "../components/common/Loading";

import api from "../api/api";

function Users() {

  const { enqueueSnackbar } = useSnackbar();

  const [users, setUsers] = useState([]);

  const [loading, setLoading] = useState(true);

  const [search, setSearch] = useState("");

  const [open, setOpen] = useState(false);

  const [selectedUser, setSelectedUser] = useState(null);

  const [deleteDialog, setDeleteDialog] = useState(false);

  const [deleteId, setDeleteId] = useState(null);

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {

    setLoading(true);

    try {

      const response = await api.get("/users");

      setUsers(response.data.data);

    } catch (error) {

      console.error(error);

    } finally {

      setLoading(false);

    }

  };

  const handleDelete = (id) => {

    setDeleteId(id);

    setDeleteDialog(true);

  };

  const confirmDelete = async () => {

    try {

      await api.delete(`/users/${deleteId}`);

      enqueueSnackbar(
        "User Deleted Successfully",
        {
          variant: "success",
        }
      );

      fetchUsers();

    } catch (error) {

      enqueueSnackbar(
        "Delete Failed",
        {
          variant: "error",
        }
      );

    }

    setDeleteDialog(false);

  };

  const handleEdit = (user) => {

    setSelectedUser(user);

    setOpen(true);

  };

  const filteredUsers = users.filter((user) =>
    user.name.toLowerCase().includes(search.toLowerCase()) ||
    user.email.toLowerCase().includes(search.toLowerCase()) ||
    user.role.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <DashboardLayout>

      {loading ? (

        <Loading />

      ) : (

        <>

          <UserToolbar
            search={search}
            setSearch={setSearch}
            setOpen={setOpen}
          />

          <UserTable
            users={filteredUsers}
            handleDelete={handleDelete}
            handleEdit={handleEdit}
          />

          <UserDialog
            open={open}
            setOpen={setOpen}
            fetchUsers={fetchUsers}
            selectedUser={selectedUser}
            setSelectedUser={setSelectedUser}
          />

          <ConfirmDialog
            open={deleteDialog}
            title="Delete User"
            message="Are you sure you want to delete this user?"
            onCancel={() => setDeleteDialog(false)}
            onConfirm={confirmDelete}
          />

        </>

      )}

    </DashboardLayout>
  );
}

export default Users;