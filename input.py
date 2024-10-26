import streamlit as st

#checkbox
st.write("점심 메뉴를 선택하세요")
짜장면 = st.checkbox("짜장면")
짬뽕 = st.checkbox("짬뽕")
탕수육 = st.checkbox("탕수육")

가격 = 0
if 짜장면:
    가격+=6000
if 짬뽕:
    가격+=7000
if 탕수육:
    가격+=12000

st.write("가격은 :",가격)

#라디오 버튼
라디오버튼 = st.radio('내가 가장 좋아하는 색상은?',
                 [":red[빨강]", ":blue[파랑]", ":green[녹색]"])

if 라디오버튼==":red[빨강]":
    st.write("빨강색을 선택하셨습니다.")

#selectbox
menu = st.selectbox("과목을 선택하세요", ['확률과 통계','미분과 적분','기하와 백터'])

st.write(menu + " 과목을 선택하셨습니다.")

#multiselect

menu2 = st.multiselect("과목을 선택하세요",
                       ['물리','생명','화학','지구과학'])

st.write(menu2)

#For 변수 in 리스트:
문자열 = ''
for a in menu2:
    문자열 += a+' '

st.write(문자열 + '과목을 선택하셨습니다.')

#문제
#물리, 생명을 선택하면
#물리 생명 과목을 선택하셨습니다.

id = st.text_input("아이디를 입력하세요",
                    placeholder="아이디 입력")
pw = st.text_input("비밀번호를 입력하세요",
                    type='password')
로그인 = st.button("로그인")

if id == 'abc' and pw == '123':
    st.write("로그인 성공")
else:
    st.write("로그인 실패")

#이미지
st.image('sunrise.png')
#동영상
st.video('https://youtu.be/S27lTdYA1QI?list=RDGMEMXdNDEg4wQ96My0DhjI-cIgVMS27lTdYA1QI')
