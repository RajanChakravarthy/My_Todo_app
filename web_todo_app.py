import streamlit as st
import functions

todos = functions.get_todo()

def add_todo():
    todo_to_add = st.session_state['new_todo'] + '\n'
    todos.append(todo_to_add.title())
    functions.write_todos(todos)

st.title("Todo App")
st.subheader("This is my Todo App.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder='Add new Todos.',
              on_change=add_todo, key='new_todo')

