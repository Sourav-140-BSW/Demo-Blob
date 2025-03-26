import { useState } from 'react';
import FileUpload from '../components/FileUpload';
import FileList from '../components/FileList';
 
const Home = () => {
  const [refreshKey, setRefreshKey] = useState(0);
 
  const handleUploadSuccess = () => {
    setRefreshKey(prevKey => prevKey + 1);
  };
 
  return (
<div className="home">
<h1>File Manager</h1>
<FileUpload onUploadSuccess={handleUploadSuccess} />
<FileList key={refreshKey} />
</div>
  );
};
 
export default Home;