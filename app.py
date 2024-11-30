import streamlit as st




st.title("python_codes")
x=st.number_input("enter a number:")

x = int(x)
##printing odd or even
if x%2==0:
    st.title(f"you have entered {x} :red[even]")
else:
    st.title(f"you have entered {x} :blue[odd]")


for i in range(2,x):
    if x%i==0:
        st.title(f"entered number {x} :rainbow[Not a prime]")
        break
else:
    st.title(f"entered number {x} :grey[prime]")