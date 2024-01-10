import streamlit as st
import pandas as pd

# Create a sample dataframe
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Location': ['New York', 'San Francisco', 'Los Angeles']
}

df = pd.DataFrame(data)

# Display the dataframe as a table
st.write(df)
