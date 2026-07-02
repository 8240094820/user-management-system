import { SnackbarProvider } from "notistack";

function AppSnackbarProvider({ children }) {
  return (
    <SnackbarProvider
      maxSnack={3}
      anchorOrigin={{
        vertical: "bottom",
        horizontal: "right",
      }}
      autoHideDuration={3000}
    >
      {children}
    </SnackbarProvider>
  );
}

export default AppSnackbarProvider;