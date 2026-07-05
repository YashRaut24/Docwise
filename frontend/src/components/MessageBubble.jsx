import './MessageBubble.css'

export function MessageBubble({ message }) {
  const isUser = message.role === 'user'

  return (
    <div className={`bubble-wrapper ${isUser ? 'user' : 'assistant'}`}>
      <div className={`bubble ${isUser ? 'bubble-user' : 'bubble-assistant'}`}>
        <p className="bubble-text">{message.text}</p>
        {!isUser && message.pages && message.pages.length > 0 && (
          <div className="page-badges">
            {message.pages.map(page => (
              <span key={page} className="page-badge">Page {page}</span>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}