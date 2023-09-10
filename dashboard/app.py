import streamlit as st

st.text('Whaddup')

st.code('for i in range(8): foo()')

# Three columns with different widths
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.write('Stands')

with col2:
    st.write('SToz')

with col3:
    st.radio('Select one:', [1, 2])