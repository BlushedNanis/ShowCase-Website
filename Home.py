import streamlit as st
from pandas import read_csv

st.set_page_config(layout='wide')

col1, col2  = st.columns(2)
with col1:
    st.image('images\photo.png')
with col2:
    st.title('BlushedNanis')
    content = """Fueled by a passion for innovation and a strong commitment to advancing automotive engineering, I bring assertiveness, insight, and
versatility to research and development. Leveraging technical expertise and a continuous learning mindset, I aim to excel in various roles,
contributing to thecompany's success. Myenthusiasm forlearning and adaptability makes me an assetto any position.
    """
    st.info(content)

st.write('Below you can find some of the apps I have built in Python. Feel free to contact me!')
st.divider()

col3, col4 = st.columns(2)
df = read_csv("data.csv", sep=';')
with col3:
    for index, row in df.iterrows():
        st.subheader(row['title'])
        st.write(row['description'])
        st.image(f"images\{row['image']}", width=600)
        st.page_link(row['url'], label=':blue[Source code]')
        if index + 1 == len(df)/2:
            break 
with col4:
    for index, row in df.iterrows():
        if index >= len(df)/2:
            st.subheader(row['title'])
            st.write(row['description'])
            st.image(f"images\{row['image']}", width=600)
            st.page_link(row['url'], label=':blue[Source code]')