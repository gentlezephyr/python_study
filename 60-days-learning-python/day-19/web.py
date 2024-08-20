import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['add_todo']
    todos.append(todo + '\n')
    functions.write_todos(todos)


st.title('My Todo App')
st.subheader('This is my todo app.')
st.write('This app is to increase your productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f'checkbox_{index}')
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f'checkbox_{index}']
        st.rerun()

st.text_input(label='Enter a todo', placeholder='Enter a todo...',
              label_visibility="hidden",
              on_change=add_todo, key='add_todo')

