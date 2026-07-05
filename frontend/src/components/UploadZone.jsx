import './UploadZone.css'

export function UploadZone({ onUpload, uploading, uploadError }) {
  const handleFileChange = (e) => {
    const file = e.target.files[0]
    if (file) onUpload(file)
  }

  const handleDrop = (e) => {
    e.preventDefault()
    const file = e.dataTransfer.files[0]
    if (file) onUpload(file)
  }

  const handleDragOver = (e) => e.preventDefault()

  return (
    <div className="upload-zone" onDrop={handleDrop} onDragOver={handleDragOver}>
      <div className="upload-icon">📄</div>
      <p className="upload-text">
        {uploading ? 'Processing PDF...' : 'Drop your PDF here or click to upload'}
      </p>
      <label className="upload-label">
        {uploading ? 'Uploading...' : 'Choose PDF'}
        <input
          type="file"
          accept=".pdf"
          onChange={handleFileChange}
          disabled={uploading}
          style={{ display: 'none' }}
        />
      </label>
      {uploadError && <p className="upload-error">{uploadError}</p>}
    </div>
  )
}