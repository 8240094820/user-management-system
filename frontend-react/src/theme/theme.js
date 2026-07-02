import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    mode: "light",

    primary: {
      main: "#2563EB",
    },

    secondary: {
      main: "#7C3AED",
    },

    success: {
      main: "#16A34A",
    },

    warning: {
      main: "#F59E0B",
    },

    error: {
      main: "#DC2626",
    },

    background: {
      default: "#F4F7FE",
      paper: "#FFFFFF",
    },
  },

  typography: {
    fontFamily: "Inter, sans-serif",

    h4: {
      fontWeight: 700,
    },

    h5: {
      fontWeight: 700,
    },

    h6: {
      fontWeight: 600,
    },

    button: {
      textTransform: "none",
      fontWeight: 600,
    },
  },

  shape: {
    borderRadius: 14,
  },

  components: {

    MuiCard: {

      styleOverrides: {

        root: {

          borderRadius: 16,

          boxShadow:
            "0 10px 25px rgba(0,0,0,0.08)",

        },

      },

    },

    MuiButton: {

      styleOverrides: {

        root: {

          borderRadius: 10,

          paddingLeft: 20,

          paddingRight: 20,

          height: 44,

        },

      },

    },

    MuiPaper: {

      styleOverrides: {

        root: {

          borderRadius: 16,

        },

      },

    },

  },

});

export default theme;