import streamlit as st
import sqlalchemy

# Initialize connection.
conn = st.experimental_connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM customers;', ttl="10m")

# Print results.
for row in df.itertuples():
    st.write(f"{row.first_name} has a :{row.ssn}:")
