import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import PreviewB from "./PreviewB.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <PreviewB />
  </StrictMode>
);
