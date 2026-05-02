# 🚀 Gemini SQL Assistant - Project

A powerful AI-driven web application that converts **natural language into SQL queries** and executes them instantly on a database.

🔗 **Live Demo:**  
👉 https://gemini-sql-assistant.streamlit.app/

---

## 📌 Overview

**Gemini SQL Assistant** is a Streamlit-based application that allows users to query databases using plain English. It leverages **Google's Gemini Generative AI model** to generate SQL queries dynamically and fetch results from a local SQLite database.

No SQL knowledge required — just ask your question.

---

## ✨ Features

- 🧠 **Natural Language to SQL**
  - Ask questions in plain English instead of writing SQL queries

- ⚡ **LLM-Powered Query Generation**
  - Uses **Gemini 2.5 Flash** via `google-generativeai`

- 📊 **Real-Time Query Execution**
  - Automatically runs generated SQL queries on SQLite database

- 🎯 **Interactive UI**
  - Built with Streamlit for a clean and intuitive experience

- 🗄️ **Self-contained Database**
  - Includes preloaded SQLite database for quick testing

---

## 🏗️ Project Structure

```

├── app.py                         # Main Streamlit application
├── sql.py                         # Database setup & sample data insertion
├── requirements.txt               # Dependencies
├── .env                           # API key configuration
├── Gemini_SQL_application.ipynb   # Experimentation & prototyping
├── Naresh_it_employee.db          # SQLite database

````

---

## ⚙️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Database:** SQLite  
- **AI Model:** Gemini 2.5 Flash  
- **API:** Google Generative AI  

---

## 🔑 Prerequisites

Before running the project, make sure you have:

- Python 3.8+
- Google Gemini API Key (from Google AI Studio)

---

## 🛠️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/gemini-sql-assistant.git
cd gemini-sql-assistant
````

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure API Key

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY="your_api_key_here"
```

---

### 4️⃣ Initialize Database

Run the setup script to create and populate the database:

```bash
python sql.py
```

---

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

The app will open at:
👉 [http://localhost:8501](http://localhost:8501)

---

## 💡 Example Queries

Try asking:

* “How many records are present?”
* “Show all employees working in Data Science role”
* “What is the total salary of Data Engineers?”
* “List employees from Pune”

---

## 🧠 How It Works

1. User enters a question in plain English
2. Gemini model converts it into SQL query
3. Query is executed on SQLite database
4. Results are displayed instantly

---

## 🔒 Environment Variables

| Variable       | Description         |
| -------------- | ------------------- |
| GOOGLE_API_KEY | Your Gemini API Key |

---

## 🚀 Future Improvements

* Support for multiple databases (MySQL, PostgreSQL)
* Query history & caching
* User authentication
* Export results (CSV / Excel)
* Fine-tuned prompt engineering for higher accuracy

---

## 🤝 Acknowledgements

Special thanks to mentors and the open-source community for guidance and support.

---

## 📬 Connect With Me

* GitHub: [https://github.com/vikrantjadhav09](https://github.com/vikrantjadhav09)
* LinkedIn: [https://www.linkedin.com/in/vikrantjadhav09/](https://www.linkedin.com/in/vikrantjadhav09/)

---

## ⭐ If You Like This Project

Give it a ⭐ on GitHub and share it with others!


