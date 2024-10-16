import streamlit as st

# Title of the app
st.title('Simple Calculator')

st.markdown("### Developed By M HUSSNAIN")

# User input for two numbers
num1 = st.number_input('Enter first number:')
num2 = st.number_input('Enter second number:')

# Selection of operation
operation = st.selectbox('Select operation', ['Add', 'Subtract', 'Multiply', 'Divide'])

# Perform calculation based on the operation
if operation == 'Add':
    result = num1 + num2
    st.write(f'Result: {result}')
elif operation == 'Subtract':
    result = num1 - num2
    st.write(f'Result: {result}')
elif operation == 'Multiply':
    result = num1 * num2
    st.write(f'Result: {result}')
elif operation == 'Divide':
    if num2 != 0:
        result = num1 / num2
        st.write(f'Result: {result}')
    else:
        st.write("Cannot divide by zero")
