import { useDocwiseUpload } from './hooks/useDocwiseUpload'
import { useDocwiseChat } from './hooks/useDocwiseChat'
import { UploadZone } from './components/UploadZone'
import { DocInfo } from './components/DocInfo'
import { ChatWindow } from './components/ChatWindow'
import './App.css'

function App() {
  const { uploading, uploadError, docInfo, uploadPdf } = useDocwiseUpload()
  const { messages, thinking, sendMessage, clearMessages } = useDocwiseChat()

  const handleReset = () => {
    window.location.reload()
  }

  return (
    <div className="app">
      <h1>Docwise</h1>
      <p className="subtitle">Chat with any PDF document</p>

      {!docInfo ? (
        <UploadZone
          onUpload={uploadPdf}
          uploading={uploading}
          uploadError={uploadError}
        />
      ) : (
        <>
          <DocInfo docInfo={docInfo} onReset={handleReset} />
          <ChatWindow
            docId={docInfo.doc_id}
            messages={messages}
            thinking={thinking}
            onSend={sendMessage}
          />
        </>
      )}
    </div>
  )
}

export default App