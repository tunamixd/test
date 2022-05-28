import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import psycopg2

conn = psycopg2.connect(**st.secrets["postgres"])

ty_tier = 'COLLAPSED MAT 2022'
py_tier = 'COLLAPSED MAT 2021'
ppy_tier = 'COLLAPSED MAT 2020'
ty_sales = 'Value Sales MAT 2022'
py_sales = 'Value Sales MAT 2021'
ppy_sales = 'Value Sales MAT 2020'

category = "SKIN CARE"
country = "USA"
segment = "FACE CARE"

company_col = "COMPANY (HARMONIZED)"
company = "P&G"

st.header('Latest Update')
option = st.radio(
    'Select Cell',
    ('Global', 'USA', 'India', 'China'))       
if option == 'Global':
    st.write("Select Option")
if option == 'USA':
    sql_query = pd.read_sql('select * from q1_2022', conn)
    df2 = pd.DataFrame(sql_query, columns = ['COUNTRY', 'CATEGORY', 'HARMONISED SEGMENT', company_col, ppy_tier, py_tier, ty_tier, ppy_sales, py_sales, ty_sales])      
    df2 = df2.loc[(df2['CATEGORY'] == category) & (df2['COUNTRY'] == country) & (df2['HARMONISED SEGMENT'] == segment)]

    masstige_ty = df2.loc[df2[ty_tier] == "MASSTIGE 200+", ty_sales].sum()
    premium_ty = df2.loc[df2[ty_tier] == "PREMIUM 120-200", ty_sales].sum()
    mass_ty = df2.loc[df2[ty_tier] == "MASS 80-120", ty_sales].sum()
    economy_ty = df2.loc[df2[ty_tier] == "ECONOMY< 80", ty_sales].sum()
    total_ty = masstige_ty + premium_ty + mass_ty + economy_ty
    masstige_py = df2.loc[df2[py_tier] == "MASSTIGE 200+", py_sales].sum()
    premium_py = df2.loc[df2[py_tier] == "PREMIUM 120-200", py_sales].sum()
    mass_py = df2.loc[df2[py_tier] == "MASS 80-120", py_sales].sum()
    economy_py = df2.loc[df2[py_tier] == "ECONOMY< 80", py_sales].sum()
    total_py = masstige_py + premium_py + mass_py + economy_py
    masstige_ppy = df2.loc[df2[ppy_tier] == "MASSTIGE 200+", ppy_sales].sum()
    premium_ppy = df2.loc[df2[ppy_tier] == "PREMIUM 120-200", ppy_sales].sum()
    mass_ppy = df2.loc[df2[ppy_tier] == "MASS 80-120", ppy_sales].sum()
    economy_ppy = df2.loc[df2[ppy_tier] == "ECONOMY< 80", ppy_sales].sum()
    total_ppy = masstige_ppy + premium_ppy + mass_ppy + economy_ppy

    market = {'Price Tier':['Economy', 'Mass', 'Premium', 'Masstige', 'Total'],
                 'MAT-2': [economy_ppy, mass_ppy, premium_ppy, masstige_ppy, total_ppy],
                 'MAT-1': [economy_py, mass_py, premium_py, masstige_py, total_py],
                 'MAT': [economy_ty, mass_ty, premium_ty, masstige_ty, total_ty]}
    df3 = pd.DataFrame(market)

    company_masstige_ty = df2.loc[(df2[ty_tier] == "MASSTIGE 200+") & (df2[company_col] == company), ty_sales].sum()
    company_premium_ty = df2.loc[(df2[ty_tier] == "PREMIUM 120-200") & (df2[company_col] == company), ty_sales].sum()
    company_mass_ty = df2.loc[(df2[ty_tier] == "MASS 80-120") & (df2[company_col] == company), ty_sales].sum()
    company_economy_ty = df2.loc[(df2[ty_tier] == "ECONOMY< 80") & (df2[company_col] == company), ty_sales].sum()
    company_total_ty = company_masstige_ty + company_premium_ty + company_mass_ty + company_economy_ty
    company_masstige_py = df2.loc[(df2[py_tier] == "MASSTIGE 200+") & (df2[company_col] == company), py_sales].sum()
    company_premium_py = df2.loc[(df2[py_tier] == "PREMIUM 120-200") & (df2[company_col] == company), py_sales].sum()
    company_mass_py = df2.loc[(df2[py_tier] == "MASS 80-120") & (df2[company_col] == company), py_sales].sum()
    company_economy_py = df2.loc[(df2[py_tier] == "ECONOMY< 80") & (df2[company_col] == company), py_sales].sum()
    company_total_py = company_masstige_py + company_premium_py + company_mass_py + company_economy_py
    company_masstige_ppy = df2.loc[(df2[ppy_tier] == "MASSTIGE 200+") & (df2[company_col] == company), ppy_sales].sum()
    company_premium_ppy = df2.loc[(df2[ppy_tier] == "PREMIUM 120-200") & (df2[company_col] == company), ppy_sales].sum()
    company_mass_ppy = df2.loc[(df2[ppy_tier] == "MASS 80-120") & (df2[company_col] == company), ppy_sales].sum()
    company_economy_ppy = df2.loc[(df2[ppy_tier] == "ECONOMY< 80") & (df2[company_col] == company), ppy_sales].sum()
    company_total_ppy = company_masstige_ppy + company_premium_ppy + company_mass_ppy + company_economy_ppy

    company = {'Price Tier':['Economy', 'Mass', 'Premium', 'Masstige', 'Total'],
                 'MAT-2': [company_economy_ppy, company_mass_ppy, company_premium_ppy, company_masstige_ppy, company_total_ppy],
                 'MAT-1': [company_economy_py, company_mass_py, company_premium_py, company_masstige_py, company_total_py],
                 'MAT': [company_economy_ty, company_mass_ty, company_premium_ty, company_masstige_ty, company_total_ty]}
    df4 = pd.DataFrame(company)

    df3.set_index('Price Tier', inplace=True)
    df4.set_index('Price Tier', inplace=True)
    share = (df4.div(df3).reset_index())
    st.write("Company Share", share)

if option == 'India':
    st.write("Under Construction")

if option == 'China':
    st.write("Under Construction")
