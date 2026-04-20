# Gemini SQL Application

This is a Streamlit-based web application that converts natural language questions (English) into SQL queries using Google's Gemini Generative AI model. It automatically executes the generated SQL query against a local SQLite database and displays the retrieved data.

## Features
- **Natural Language to SQL**: Ask questions about your data in plain English instead of writing complex SQL queries manually.
- **LLM Powered**: Leverages the powerful `gemini-2.5-flash` model via the `google-generativeai` API.
- **Interactive UI**: An intuitive query interface built using Streamlit.
- **Local Database Engine**: Includes a self-contained SQLite database for rapid testing and demonstration.

## Project Structure
- `app.py`: The main Streamlit application containing the frontend interface and logic to fetch from the Gemini model & query the database.
- `sql.py`: A setup script to initialize the SQLite database (`Naresh_it_employee.db`), create the `Naresh_it_employee` table, and populate it with sample employee records.
- `requirements.txt`: Python package dependencies for the project.
- `.env`: Configuration file for environment variables (used to store the Gemini API Key securely).
- `Gemini_SQL_application.ipynb`: A Jupyter notebook likely used for initial local testing and prototyping.
- `Naresh_it_employee.db`: The created local SQLite database instance.

## Prerequisites

Before running the application, ensure you have Python installed. You will also need an active [Google AI Studio API Key](https://aistudio.google.com/).

## Setup Instructions

1. **Install Dependencies**
   Install the required Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Key**
   You need a Google Gemini API key to query the Generative AI model. 
   - Ensure the `.env` file exists in the root directory.
   - Open `.env` and add your Google API key like this:
     ```env
     GOOGLE_API_KEY="your_api_key_here"
     ```

3. **Initialize the Database**
   Before running the app, you need to create the SQLite database and populate records. Run the provided setup script once:
   ```bash
   python sql.py
   ```
   This will run data insertion routines and create a `Naresh_it_employee.db` file within the directory.

4. **Run the Streamlit Application**
   Launch the web app via Streamlit:
   ```bash
   streamlit run app.py
   ```
   This will start a local server and open the application in your default web browser (typically at `http://localhost:8501`).

## Example Questions

Once the app is running in your browser, try inputting a natural language question into the text box. For instance:
- *"How many entries of records are present?"*
- *"Tell me all the employees working in Data Science role?"*
- *"What is the total salary of Data Engineers?"*

Click on **Ask the question** to view the retrieved database results iteratively under the inputs.
