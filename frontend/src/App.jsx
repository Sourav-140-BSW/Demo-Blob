import { useState } from "react";
import FileUpload from "./components/FileUpload";
import FileList from "./components/FileList";

function App() {
  const [refresh, setRefresh] = useState(false);

  const handleUploadSuccess = () => {
    setRefresh(!refresh); // Trigger file list refresh
  };

  return (
    <div className="app">
      <h1>File Upload and Download</h1>
      <FileUpload onUploadSuccess={handleUploadSuccess} />
      <FileList key={refresh} />
    </div>
  );
}

export default App;
