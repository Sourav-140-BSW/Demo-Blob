import { useState } from "react";
import { uploadFile } from "../api";

const FileUpload = ({ onUploadSuccess }) => {
  const [file, setFile] = useState(null);
  const [isUploading, setIsUploading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

    setIsUploading(true);
    try {
      await uploadFile(file);
      onUploadSuccess(); // Refresh file list
      setFile(null);
      e.target.reset();
    } catch (error) {
      console.error("Upload failed:", error);
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <div className="file-upload">
      <h2>Upload File</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit" disabled={!file || isUploading}>
          {isUploading ? "Uploading..." : "Upload"}
        </button>
      </form>
    </div>
  );
};

export default FileUpload;
