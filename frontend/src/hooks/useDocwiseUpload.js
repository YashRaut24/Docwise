import { useState } from 'react'

const API_URL = 'http://localhost:8001'

export function useDocwiseUpload() {
  const [uploading, setUploading] = useState(false)
  const [uploadError, setUploadError] = useState(null)
  const [docInfo, setDocInfo] = useState(null)

  const uploadPdf = async (file) => {
    if (!file) return
    setUploading(true)
    setUploadError(null)

    const formData = new FormData()
    formData.append('file', file)

    try {
      const response = await fetch(`${API_URL}/upload`, {
        method: 'POST',
        body: formData
      })
      const data = await response.json()

      if (data.error) {
        setUploadError(data.error)
        return
      }

      setDocInfo(data)
    } catch (err) {
      setUploadError('Upload failed. Is the backend running?')
    } finally {
      setUploading(false)
    }
  }

  return { uploading, uploadError, docInfo, uploadPdf }
}