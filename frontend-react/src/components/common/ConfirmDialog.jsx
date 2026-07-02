import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  Typography,
} from "@mui/material";

function ConfirmDialog({
  open,
  title,
  message,
  onCancel,
  onConfirm,
}) {
  return (
    <Dialog
      open={open}
      onClose={onCancel}
      maxWidth="xs"
      fullWidth
    >
      <DialogTitle>
        {title}
      </DialogTitle>

      <DialogContent>
        <Typography>
          {message}
        </Typography>
      </DialogContent>

      <DialogActions>

        <Button
          onClick={onCancel}
        >
          Cancel
        </Button>

        <Button
          variant="contained"
          color="error"
          onClick={onConfirm}
        >
          Delete
        </Button>

      </DialogActions>
    </Dialog>
  );
}

export default ConfirmDialog;