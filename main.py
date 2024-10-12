# # import streamlit as st

# # st. title("welcome to nikki tech")


# import streamlit as st

# st.write("Welcome to your first Streamlit app.")

import streamlit as st

st.title("welcome  to nikki tech")

name = st. text_input("enter your Name :")
fname = st. text_input("enter your Father name :")
adr = st. text_area("enter your text :")
classdata = st. selectbox("enter you Class :",(1,2,3,4,5,6,7,8,9))


button = st.button("Done")
if button :
    st. markdown(f"""
                 Name : {name}
                 Father Name : {fname}
                 address : {adr}
                 class : {classdata}""")

