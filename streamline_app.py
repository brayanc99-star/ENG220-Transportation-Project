#just TEST
import streamlit as st
import pandas as pd

st.title("Project Cuba Corridor")
st.write("Safety and access along US 550 near Cuba, NM")

data = pd.DataFrame({
    "Year": [2010, 2020],
    "Population": [731, 628],
})

st.subheader("Cuba population")
st.bar_chart(data, x="Year", y="Population")
