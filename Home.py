import streamlit as st
from pandas import read_csv


# Set page config as wide
st.set_page_config(layout='wide')

# Set 2 columns for user info
col1, col2  = st.columns(2)
with col1:
    st.image('images\\photo.jpg', width=500)
with col2:
    st.title('BlushedNanis')
    content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer rhoncus quam sed magna convallis posuere. Morbi eu tempus justo. Ut tristique orci a ipsum imperdiet, 
ac fermentum libero aliquam. Maecenas eu tellus non enim euismod malesuada eu non dui. Vivamus ut ipsum ante. Integer sed lacus a dolor tincidunt luctus. Duis felis nisi, vestibulum 
sed cursus ac, vestibulum vitae neque. Maecenas bibendum blandit diam, eu lobortis nunc varius sed.

Interdum et malesuada fames ac ante ipsum primis in faucibus. Nam luctus, dolor non consectetur aliquet, est ligula suscipit enim, nec aliquam odio nisl interdum magna. Nulla viverra 
est vitae varius maximus. Fusce finibus arcu ipsum, pulvinar aliquet quam convallis nec. Quisque a arcu ante. Aenean ac erat non lacus hendrerit fermentum cursus eu erat. Praesent 
placerat eros a lectus convallis sollicitudin. Etiam ipsum turpis, bibendum et convallis id, condimentum ac erat. Ut pellentesque nibh felis, quis tincidunt orci efficitur ac. 
Proin ullamcorper nulla est. Praesent quis magna feugiat, dapibus ante nec, elementum neque. Nullam non pharetra nunc, sed lacinia risus. Integer sed ligula pellentesque, consequat 
enim nec, consectetur mauris. Ut urna ex, luctus vestibulum convallis eget, cursus et erat."""
    st.info(content)

st.write('Below you can find some of the apps I have built in Python. Feel free to contact me!')
st.divider()

# Set for projects showcase
col3, col4 = st.columns(2)

# Read projects data
df = read_csv("data.csv", sep=';')

with col3:
    # Add the first half of the projects into the first column
    for index, row in df.iterrows():
        st.subheader(row['title'])
        st.write(row['description'])
        st.image(f"images\{row['image']}", width=600)
        st.page_link(row['url'], label=':blue[Source code]')
        if index + 1 == len(df)/2:
            break 
        
with col4:
    #Add the seconds half of the projects on the second column
    for index, row in df.iterrows():
        if index >= len(df)/2:
            st.subheader(row['title'])
            st.write(row['description'])
            st.image(f"images\{row['image']}", width=600)
            st.page_link(row['url'], label=':blue[Source code]')