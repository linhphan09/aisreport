import streamlit as st
import pandas as pd
import psycopg2

@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgresql"])
conn = init_connection()
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
rows = run_query("SELECT * FROM customers LIMIT 10")
data = pd.DataFrame(rows)
data.columns=['ssn','first_name','country']
st.table(data)
