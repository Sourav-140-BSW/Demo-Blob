// const API_BASE_URL = "https://klarifai-backend-bbsr-cydgehd0hmgxcybk.centralindia-01.azurewebsites.net/api";

// // ✅ Upload File
// export const uploadFile = async (file) => {
//   const formData = new FormData();
//   formData.append("file", file);
//   formData.append("name", file.name); // ✅ Ensure 'name' is sent

//   const response = await fetch(`${API_BASE_URL}/files/upload/`, {
//     method: "POST",
//     body: formData,
//     credentials: "include",
//   });

//   if (!response.ok) {
//     throw new Error(`Upload failed: ${response.statusText}`);
//   }

//   return response.json();
// };

// // ✅ Get List of Files
// export const getFiles = async () => {
//   const response = await fetch(`${API_BASE_URL}/files/`);
//   if (!response.ok) {
//     throw new Error(`Error fetching files: ${response.statusText}`);
//   }
//   return response.json();
// };

// // ✅ Download File (Fix Missing Export)
// export const downloadFile = async (id, name) => {
//   const response = await fetch(`${API_BASE_URL}/files/${id}/`, {
//     method: "GET",
//   });

//   if (!response.ok) {
//     throw new Error(`Download failed: ${response.statusText}`);
//   }

//   const blob = await response.blob();
//   const url = window.URL.createObjectURL(blob);
//   const link = document.createElement("a");
//   link.href = url;
//   link.setAttribute("download", name);
//   document.body.appendChild(link);
//   link.click();
//   link.remove();
// };


// api.js
const API_BASE_URL = "https://klarifai-backend-bbsr-cydgehd0hmgxcybk.centralindia-01.azurewebsites.net/api";

// Upload File
export const uploadFile = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(`${API_BASE_URL}/files/upload/`, {
    method: "POST",
    body: formData,
    credentials: "include",
  });

  if (!response.ok) {
    throw new Error(`Upload failed: ${response.statusText}`);
  }

  return response.json();
};

// Get List of Files
export const getFiles = async () => {
  const response = await fetch(`${API_BASE_URL}/files/`);
  if (!response.ok) {
    throw new Error(`Error fetching files: ${response.statusText}`);
  }
  return response.json();
};

// Download File
export const downloadFile = async (id, name) => {
  const response = await fetch(`${API_BASE_URL}/files/${id}/`);
  
  if (!response.ok) {
    throw new Error(`Download failed: ${response.statusText}`);
  }

  const data = await response.json();
  // Redirect to Azure Blob URL
  window.open(data.url, '_blank');
};

// Delete File
export const deleteFile = async (id) => {
  const response = await fetch(`${API_BASE_URL}/files/${id}/delete/`, {
    method: "DELETE",
    credentials: "include",
  });

  if (!response.ok) {
    throw new Error(`Delete failed: ${response.statusText}`);
  }

  return response.json();
};