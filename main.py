import streamlit as st

#1. 자기소개
#자

st.write("TEST")
st.header(":violet[제목]")
st.subheader("1.공동교육과정")
st.write("매천고등학교의 공동교육과정 입니다.")
st.code("print('Hello, World!!!')", language='python')
st.divider()
st.markdown(":red[**공동**]교육과정 :blue[매천고등학교]")

button = st.button("버튼")
if button:
    st.write("버튼클릭!!!")

btnmulti = st.button("곱하기")
multia = st.number_input("1번 숫자를 입력하세요", step=1, key="multi_a")
multib = st.number_input("2번 숫자를 입력하세요", step=1, key="multi_b")
if btnmulti :
    st.write(multia * multib)

#1과제
#사칙연산하는 프로그램을 만들어보세요!
#버튼 +, -, *, / 
#두 수를 계산하는 프로그램을 만듭니다.
#50분까지(쉬는시간 포함)
