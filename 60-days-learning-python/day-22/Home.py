import streamlit as st
import pandas

st.set_page_config(page_title='Home', layout='wide')

st.title('The Best Company')

text_content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ut nisi vitae ligula 
sollicitudin tincidunt. Proin viverra odio a metus lacinia congue. In non felis orci. Pellentesque sit amet lacus sit 
amet purus consectetur condimentum in nec nunc. Morbi posuere eu libero ac euismod. In a ultricies nisi. Pellentesque 
luctus euismod mauris, ac fermentum felis blandit sit amet."""

st.write(text_content)

st.header('Our Team')

col1, col2, col3 = st.columns(3)

df = pandas.read_csv('60-days-learning-python/day-22/004 data.csv')

with col1:
    for index, person in df[:4].iterrows():
        st.subheader(f'{person['first name']} {person['last name']}'.title())
        st.text(person['role'])
        st.image(f"60-days-learning-python/day-22/images/{person['image']}")

with col2:
    for index, person in df[4:8].iterrows():
        st.subheader(f'{person['first name']} {person['last name']}'.title())
        st.text(person['role'])
        st.image(f"60-days-learning-python/day-22/images/{person['image']}")

with col3:
    for index, person in df[8:12].iterrows():
        st.subheader(f'{person['first name']} {person['last name']}'.title())
        st.text(person['role'])
        st.image(f"60-days-learning-python/day-22/images/{person['image']}")

