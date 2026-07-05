import { useState } from 'react'

const API_URL = 'http://localhost:8001'

export function useDocwiseChat() {
  const [messages, setMessages] = useState([])
  const [thinking, setThinking] = useState(false)

  const sendMessage = async (docId, question) => {
    if (!question.trim()) return

    const userMessage = { role: 'user', text: question }
    setMessages(prev => [...prev, userMessage])
    setThinking(true)

    try {
      const response = await fetch(`${API_URL}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ doc_id: docId, question })
      })
      const data = await response.json()

      const assistantMessage = {
        role: 'assistant',
        text: data.answer,
        pages: data.pages_used
      }
      setMessages(prev => [...prev, assistantMessage])
    } catch (err) {
      setMessages(prev => [...prev, {
        role: 'assistant',
        text: 'Something went wrong. Please try again.',
        pages: []
      }])
    } finally {
      setThinking(false)
    }
  }

  const clearMessages = () => setMessages([])

  return { messages, thinking, sendMessage, clearMessages }
}