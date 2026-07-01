# 🤖 Enhanced Q&A Chatbot with OpenAI

An interactive **Q&A Chatbot** built using **Streamlit**, **LangChain**, and **OpenAI GPT models**. The application allows users to ask questions, choose the OpenAI model, adjust generation parameters like **temperature** and **maximum tokens**, and receive AI-generated responses in real time.

The project also includes **LangSmith tracing**, enabling you to monitor, debug, and analyze every LLM call made by the application.

---

## 🚀 Features

- 💬 Interactive Q&A interface built with Streamlit
- 🤖 Supports multiple OpenAI models
  - GPT-4 Turbo
  - GPT-4
  - GPT-4o
  - GPT-4o Mini
- 🌡️ Adjustable Temperature
- 📝 Configurable Maximum Token Limit
- 🔗 Built using LangChain Expression Language (LCEL)
- 📊 LangSmith integration for tracing and debugging
- 🔒 Secure API key input through the Streamlit sidebar

---

## 🛠️ Tech Stack

- Python 3.12+
- Streamlit
- LangChain
- LangChain OpenAI
- OpenAI
- LangSmith
- python-dotenv

---

## 📂 Project Structure

```text
.
├── app.py
├── .env
├── pyproject.toml
├── README.md
└── .venv/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/AnushkJain2201/Q-A-Chatbot-Using-OpenAI-And-Ollama.git
cd Q-A-Chatbot-Using-OpenAI-And-Ollama
```

### 2. Create a virtual environment

Using **uv**

```bash
uv venv
```

Activate it

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

---

### 3. Install dependencies

Using **uv**

```bash
uv sync
```

or

```bash
uv pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root and add the following variables:

```env
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_PROJECT=Enhanced-QA-Chatbot
```

### What these variables are used for

| Variable | Description |
|----------|-------------|
| `LANGCHAIN_API_KEY` | Your LangSmith API Key used for tracing |
| `LANGSMITH_ENDPOINT` | LangSmith API endpoint |
| `LANGCHAIN_PROJECT` | Name of the project displayed inside LangSmith |

> **Note:** These variables are optional if you don't want tracing. However, they are recommended for monitoring and debugging your LangChain applications.

---

## ▶️ Running the Application

Start the Streamlit app

```bash
streamlit run app.py
```

or, if using **uv**

```bash
uv run streamlit run app.py
```

---

## 📖 How to Use

1. Launch the application.
2. Enter your **OpenAI API Key** in the sidebar.
3. Select the desired OpenAI model.
4. Adjust the Temperature and Max Tokens if required.
5. Type your question.
6. Click **Generate Response**.
7. View the AI-generated answer.

---

## 📊 LangSmith Tracing

This project is integrated with **LangSmith**, allowing you to:

- Trace every LLM call
- Inspect prompts
- Analyze responses
- Debug LangChain pipelines
- Monitor token usage

---

## 📸 Demo

*(Add screenshots or a GIF here once available.)*

---

## 📚 Concepts Used

- LangChain Expression Language (LCEL)
- Prompt Templates
- Output Parsers
- ChatOpenAI
- Streamlit Components
- Environment Variables
- LangSmith Tracing

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.