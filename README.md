# LangChain OpenAI Chatbot

A Streamlit-based chatbot implementation using LangChain and OpenAI's GPT-3.5 model. This application demonstrates the integration of modern AI capabilities with a user-friendly web interface.

![alt text](https://github.com/Pranava-Kailash/Langchain_Basic_Chatbot/blob/main/StreamLit%20Front%20End.png)


## 🌟 Features

- Interactive chat interface using Streamlit
- Integration with OpenAI's GPT-3.5 model
- Environment variable management for secure API key handling
- Structured prompt templating using LangChain
- Clean and simple user interface

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/langchain-openai-chatbot.git
cd langchain-openai-chatbot
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # For Linux/Mac
# OR
.venv\Scripts\activate  # For Windows
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with your API keys:

```
OPENAI_API_KEY=your_openai_api_key
LANGSMITH_TRACING=your_langsmith_tracing_key
LANGSMITH_API_KEY=your_langsmith_api_key
```

## 📁 Project Structure

```
langchain-openai-chatbot/
├── app.py
├── .env
├── requirements.txt
└── README.md
```

## 💻 Usage

1. Ensure all requirements are installed and `.env` file is configured
2. Run the Streamlit application:

```bash
streamlit run app.py
```

3. Open your browser and navigate to the provided local URL (typically `http://localhost:8501`)
4. Enter your question in the text area and click "Ask" to get a response

## 📝 Code Overview

The main application (`app.py`) consists of:

- Environment setup and configuration
- ChatPromptTemplate initialization for structured prompts
- Streamlit UI implementation
- OpenAI model integration through LangChain
- Response parsing and display logic

## 🔑 Environment Variables

The following environment variables are required:

- `OPENAI_API_KEY`: Your OpenAI API key
- `LANGSMITH_TRACING`: LangSmith tracing configuration
- `LANGSMITH_API_KEY`: LangSmith API key

## 🛡️ Dependencies

Here's the `requirements.txt` for the project:

```txt
langchain-openai>=0.0.2
langchain-core>=0.1.4
streamlit>=1.29.0
python-dotenv>=1.0.0
```

## ⚠️ Prerequisites

- Python 3.8 or higher
- OpenAI API key
- LangSmith account (for tracing capabilities)
