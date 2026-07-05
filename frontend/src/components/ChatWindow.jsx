import { useEffect, useRef, useState } from 'react'
import { MessageBubble } from './MessageBubble'
import './ChatWindow.css'

export function ChatWindow({ docId, messages, thinking, onSend }) {
  const [input, setInput] = useState('')
  const bottomRef = useRef(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, thinking])

  const handleSubmit = (e) => {
    e.preventDefault()
    if (!input.trim()) return
    onSend(docId, input)
    setInput('')
  }

  return (
    <div className="chat-window">
      <div className="messages">
        {messages.length === 0 && (
          <p className="empty-state">Ask anything about your document...</p>
        )}
        {messages.map((msg, i) => (
          <MessageBubble key={i} message={msg} />
        ))}
        {thinking && (
          <div className="bubble-wrapper assistant">
            <div className="bubble bubble-assistant thinking">
              <span>Thinking</span>
              <span className="dots">...</span>
            </div>
          </div>
        )}
        <div ref={bottomRef} />
      </div>

      <form onSubmit={handleSubmit} className="chat-input-form">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask a question about your PDF..."
          className="chat-input"
          disabled={thinking}
        />
        <button type="submit" disabled={thinking} className="send-button">
          Send
        </button>
      </form>
    </div>
  )
}