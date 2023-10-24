import streamlit as st
import pandas as pd

# Initialize connection.
conn = st.experimental_connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM customers LIMIT 10;', ttl="10m")
df = pd.DataFrame(rows)
df.columns=['ssn','first_name','country']
st.table(data)
