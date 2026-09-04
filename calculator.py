#pip install streamlit
#to run :-m streamlit run calculator.py
import streamlit as st

st.title("Streamlit Calculator")
#st.subheader("this is a simple calculator build with streamlit")
st.markdown("This is a simple calculator build with streamlit")

c1,c2 = st.columns(2)
fnum = c1.number_input("enter first number",value =0)
snum = c2.number_input("enter second number",value=0)

option = ("select operation",("addition","subtraction","multiplication","division"))
choice = st.selectbox("select operation",option)

button = st.button("calculate")
result = 0
if button:
    if choice == "addition":
        result = fnum + snum
    elif choice == "subtraction":
        result = fnum - snum
    elif choice == "multiplication":
        result = fnum * snum
    elif choice == "division":
        result = fnum / snum
    else:
        st.success("result:" + str(result))

#st.ballons()
st.snow()