# Chat with Website

A chatbot application that lets you interact with the content of any website using its URL as context. Built with Python, Streamlit, and Langchain, it leverages LLMs to answer your questions based on the website's content.

## Features

- Enter any website URL and chat with its content
- Uses Langchain for document loading, splitting, and retrieval
- Embeds website text into a vector store for efficient context retrieval
- Maintains chat history for context-aware responses
- Simple Streamlit web interface

## How It Works

1. **Load Website Content:**  
   The app fetches and parses the content of the provided URL.
2. **Chunk & Embed:**  
   The content is split into manageable chunks and embedded into a vector store (ChromaDB) using OpenAI embeddings.
3. **Conversational Retrieval:**  
   User queries are processed in context (with chat history) and relevant website chunks are retrieved.
4. **LLM Response:**  
   The retrieved context is passed to a language model (OpenAI) to generate a response.

## Folder Structure

```
chat-with-website/
│
├── .env                # Environment variables (API keys, etc.)
├── .gitignore
└── src/
    ├── app.py          # Main Streamlit app
    └── check.py        # Utility for inspecting document chunks
```

## Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key (set in `.env` as `OPENAI_API_KEY`)

### Installation

1. **Clone the repository:**

   ```sh
   git clone <repo-url>
   cd chat-with-website
   ```

2. **Install dependencies:**

   ```sh
   pip install streamlit langchain langchain-openai beautifulsoup4 python-dotenv chromadb
   ```

3. **Set up environment variables:**
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

### Running the App

```sh
streamlit run src/app.py
```

- Open your browser to the provided local URL.
- Enter a website URL in the sidebar and start chatting!

## Notes

- The first time you enter a URL, the app fetches and processes the website, which may take a few seconds.
- All chat history is session-based and resets when you reload the app.

## License

This project is for educational purposes.
