from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import pandas as pd
import google.generativeai as genai

# Configure Gemini
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("❌ GOOGLE_API_KEY not found in .env file")
    st.stop()

genai.configure(api_key=api_key)

# ---------- Helper Functions ----------

def get_gemini_response(question, prompt):
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content([prompt[0], question])
        return response.text.strip()
    except Exception as e:
        st.error(f"Gemini API error: {e}")
        return None

def is_safe_query(sql):
    forbidden = ["DROP", "DELETE", "INSERT", "UPDATE", "ALTER", "CREATE"]
    return not any(word in sql.upper() for word in forbidden)

def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        df = pd.read_sql_query(sql, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"SQL Error: {e}")
        return None

def get_schema_info(db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cur.fetchall()
        schema = {}
        for (table_name,) in tables:
            cur.execute(f"PRAGMA table_info({table_name});")
            columns = cur.fetchall()
            schema[table_name] = [
                {"name": col[1], "type": col[2]} for col in columns
            ]
            cur.execute(f"SELECT * FROM {table_name} LIMIT 3;")
            preview = cur.fetchall()
            schema[table_name + "_preview"] = preview
        conn.close()
        return schema
    except Exception as e:
        st.sidebar.error(f"Schema load error: {e}")
        return {}

# ---------- Prompt ----------

prompt = [
    """
    You are an expert in converting English questions to SQL queries.
    The SQL database is named Naresh_it_employee and has these columns:
    employee_name, employee_role, employee_salary.

    Examples:
    - "How many records?" → SELECT COUNT(*) FROM Naresh_it_employee;
    - "All Data Science employees?" → SELECT * FROM Naresh_it_employee WHERE employee_role='Data Science';

    Rules:
    - Return ONLY the raw SQL query, no markdown, no ```sql blocks, no explanation.
    - Only use SELECT statements.
    """
]

# ---------- Streamlit UI ----------

st.set_page_config(page_title="SQL Query Assistant", page_icon="🧠", layout="wide")
st.title("🧠 Gemini SQL Query Assistant")
st.caption("Ask questions in plain English — get answers from the database.")

# ✅ NEW: Welcome Modal on first load using session_state
if "show_welcome" not in st.session_state:
    st.session_state.show_welcome = True

@st.dialog("👋 Welcome to Gemini SQL Query Assistant!")
def show_welcome_modal():
    st.markdown("""
    ### 🤔 What does this app do?
    This app lets you **ask questions in plain English** and get answers 
    directly from the employee database — no SQL knowledge needed!

    ---

    ### 🗄️ About the Database
    You are querying the **Naresh IT Employee** database with these columns:

    | Column | Type | Description |
    |---|---|---|
    | `employee_name` | TEXT | Full name of the employee |
    | `employee_role` | TEXT | Job role / department |
    | `employee_salary` | INTEGER | Monthly salary in ₹ |

    ---

    ### 💡 Example Questions You Can Ask

    **Count & Stats:**
    - How many employees are there?
    - What is the average salary of all employees?
    - Who has the highest salary?

    **Filter & Search:**
    - Show all employees in the Data Science role
    - List employees with salary greater than 50000
    - Who works as a Data Analyst?

    **Sorting:**
    - Show all employees sorted by salary
    - List top 5 highest paid employees

    ---

    ### ⚠️ Things to Keep in Mind
    - Only **read (SELECT)** queries are allowed — no edits to the database
    - Be specific with role names (e.g. *Data Science*, *Data Analyst*)
    - If no results appear, try rephrasing your question

    ---
    """)

    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🚀 Get Started!", use_container_width=True, type="primary"):
            st.session_state.show_welcome = False
            st.rerun()

# Show modal only on first load
if st.session_state.show_welcome:
    show_welcome_modal()

# ✅ Help button to reopen modal anytime
with st.sidebar:

    st.markdown("**💡 Example Questions:**")
    examples = [
        "How many employees are there?",
        "Show all employees in Data Science role",
        "Who has the highest salary?",
        "List employees with salary greater than 50000",
        "How many unique roles are there?",
    ]
    for q in examples:
        st.markdown(f"- {q}")

    st.divider()

    # ✅ Reopen welcome guide anytime
    if st.button("📖 Show Guide Again", use_container_width=True):
        st.session_state.show_welcome = True
        st.rerun()

# ---------- Main Input ----------

question = st.text_input("Ask your question:", placeholder="e.g. Show all employees with salary > 50000")

if st.button("🔍 Ask", use_container_width=True):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating SQL..."):
            sql = get_gemini_response(question, prompt)

        if sql:
            st.subheader("Generated SQL")
            st.code(sql, language="sql")

            if not is_safe_query(sql):
                st.error("⚠️ Unsafe query detected. Only SELECT queries are allowed.")
            else:
                with st.spinner("Fetching results..."):
                    df = read_sql_query(sql, "Naresh_it_employee.db")

                if df is not None:
                    if df.empty:
                        st.info("No records found.")
                    else:
                        st.subheader(f"Results ({len(df)} rows)")
                        st.dataframe(df, use_container_width=True)