import React from "react";
import ReactDOM from "react-dom/client";

import App from "./App";

import "./index.css";

import ThemeContextProvider from "./contexts/ThemeContext";
import AppSnackbarProvider from "./components/common/SnackbarProvider";

ReactDOM.createRoot(
  document.getElementById("root")
).render(
  <React.StrictMode>

    <ThemeContextProvider>

      <AppSnackbarProvider>

        <App />

      </AppSnackbarProvider>

    </ThemeContextProvider>

  </React.StrictMode>
);