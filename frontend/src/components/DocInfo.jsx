import './DocInfo.css'

export function DocInfo({ docInfo, onReset }) {
  return (
    <div className="doc-info">
      <div className="doc-details">
        <span className="doc-icon">📄</span>
        <div>
          <p className="doc-name">{docInfo.filename}</p>
          <p className="doc-meta">{docInfo.page_count} pages · {docInfo.chunks_created} chunks indexed</p>
        </div>
      </div>
      <button onClick={onReset} className="reset-button">Upload New PDF</button>
    </div>
  )
}