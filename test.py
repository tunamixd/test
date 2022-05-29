import streamlit as st
import pandas as pd
import psycopg2

conn = psycopg2.connect(**st.secrets["postgres"])

st.header('Latest Update')
option = st.radio(
    'Select Cell',
    ('Global', 'USA', 'India', 'China'))       
if option == 'Global':
    st.write("Select Option")
if option == 'USA':
    df = pd.read_sql_query('SELECT * FROM q1_2022', conn)
    st.write(df.columns.values)
if option == 'India':
    st.write("Under Construction")
if option == 'China':
    st.write("Under Construction")
