// import { useState, useEffect } from "react";
// import { getFiles, downloadFile } from "../api";



// const FileList = () => {
//   const [files, setFiles] = useState([]);
//   const [isLoading, setIsLoading] = useState(true);

//   const fetchFiles = async () => {
//     setIsLoading(true);
//     try {
//       const data = await getFiles();
//       setFiles(data);
//     } catch (error) {
//       console.error("Error fetching files:", error);
//     } finally {
//       setIsLoading(false);
//     }
//   };

//   const handleDownload = async (id, name) => {
//     try {
//       await downloadFile(id, name);
//     } catch (error) {
//       console.error("Download failed:", error);
//     }
//   };

//   useEffect(() => {
//     fetchFiles();
//   }, []);

//   if (isLoading) return <div>Loading files...</div>;

//   return (
//     <div className="file-list">
//       <h2>Files</h2>
//       {files.length === 0 ? (
//         <p>No files uploaded yet.</p>
//       ) : (
//         <ul>
//           {files.map((file) => (
//             <li key={file.id}>
//               <span>{file.name}</span>
//               <button onClick={() => handleDownload(file.id, file.name)}>
//                 Download
//               </button>
//             </li>
//           ))}
//         </ul>
//       )}
//     </div>
//   );
// };

// export default FileList;


// FileList.jsx
import { useState, useEffect } from "react";
import { getFiles, downloadFile, deleteFile } from "../api";

const FileList = ({ refresh, setRefresh }) => {
  const [files, setFiles] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  const fetchFiles = async () => {
    setIsLoading(true);
    try {
      const data = await getFiles();
      setFiles(data);
    } catch (error) {
      console.error("Error fetching files:", error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleDownload = async (id, name) => {
    try {
      await downloadFile(id, name);
    } catch (error) {
      console.error("Download failed:", error);
    }
  };

  const handleDelete = async (id) => {
    try {
      await deleteFile(id);
      setRefresh(!refresh); // Trigger refresh
    } catch (error) {
      console.error("Delete failed:", error);
    }
  };

  useEffect(() => {
    fetchFiles();
  }, [refresh]);

  if (isLoading) return <div>Loading files...</div>;

  return (
    <div className="file-list">
      <h2>Files</h2>
      {files.length === 0 ? (
        <p>No files uploaded yet.</p>
      ) : (
        <ul>
          {files.map((file) => (
            <li key={file.id}>
              <span>{file.name}</span>
              <button onClick={() => handleDownload(file.id, file.name)}>
                Download
              </button>
              <button onClick={() => handleDelete(file.id)}>
                Delete
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default FileList;