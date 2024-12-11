# Import all the requirement libraries

import pandas as pd
import plotly.express as px
import streamlit as st

# Configuration of the Page
st.set_page_config(
    page_title="RevealX",
    page_icon="🔍"
)

st.title(":red[RevealX]")
st.subheader("Reveal the Pattern and Insights :red[RevealX]")

file = st.file_uploader("Drop your csv or  Excel File here",type=['csv','xlsx'])
if(file!=None):
    if(file.name.endswith('csv')):
        data = pd.read_csv(file)
    else:
        data=pd.read_excel(file)
    st.info("The file has been Uploaded Successfully",icon='✔️')
    st.dataframe(data)
