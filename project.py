import streamlit as st
pages = {
    "회원" : [
        st.Page("./page/a.py",title="로그인"),
        st.Page("./page/b.py",title="로그아웃")
    ],
    "   회원정보":[
        st.Page("./page/c.py",title="내 주소 불러오기"),
        st.Page("./page/d.py",title="내 주소 수정하기")
    ],
    "우리 지역 버스 찾기":[
        st.Page("./page/e.py",title="정거장 별 정보 조회"),
        st.Page("./page/f.py",title="일간 통행량 조회"),
        st.Page("./page/g.py",title="시간표/배차 조회")
    ]
}

pg = st.navigation(pages)
pg.run()
