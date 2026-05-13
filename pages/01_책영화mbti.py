import streamlit as st

st.set_page_config(
    page_title="MBTI 책 & 영화 추천",
    page_icon="📚"
)

st.title("📚🎬 MBTI별 책 & 영화 추천")
st.write("MBTI를 선택하면 어울리는 인기 책과 영화를 추천해드립니다!")

# MBTI 데이터
mbti_data = {
    "INTJ": {
        "books": [
            "세이노의 가르침",
            "마흔에 읽는 쇼펜하우어"
        ],
        "movies": [
            "오펜하이머",
            "듄"
        ]
    },
    "INTP": {
        "books": [
            "역행자",
            "물고기는 존재하지 않는다"
        ],
        "movies": [
            "인터스텔라",
            "테넷"
        ]
    },
    "ENTJ": {
        "books": [
            "원씽",
            "트렌드 코리아 2025"
        ],
        "movies": [
            "탑건: 매버릭",
            "아이언맨"
        ]
    },
    "ENTP": {
        "books": [
            "아주 작은 습관의 힘",
            "퓨처 셀프"
        ],
        "movies": [
            "에브리씽 에브리웨어 올 앳 원스",
            "가디언즈 오브 갤럭시"
        ]
    },
    "INFJ": {
        "books": [
            "불편한 편의점",
            "죽고 싶지만 떡볶이는 먹고 싶어"
        ],
        "movies": [
            "소울",
            "엘리멘탈"
        ]
    },
    "INFP": {
        "books": [
            "모순",
            "아몬드"
        ],
        "movies": [
            "웡카",
            "코코"
        ]
    },
    "ENFJ": {
        "books": [
            "데일 카네기 인간관계론",
            "기분이 태도가 되지 않게"
        ],
        "movies": [
            "인사이드 아웃 2",
            "기생충"
        ]
    },
    "ENFP": {
        "books": [
            "나는 나로 살기로 했다",
            "하버드 상위 1퍼센트의 비밀"
        ],
        "movies": [
            "바비",
            "라라랜드"
        ]
    },
    "ISTJ": {
        "books": [
            "부자 아빠 가난한 아빠",
            "돈의 속성"
        ],
        "movies": [
            "서울의 봄",
            "범죄도시4"
        ]
    },
    "ISFJ": {
        "books": [
            "어서 오세요, 휴남동 서점입니다",
            "달러구트 꿈 백화점"
        ],
        "movies": [
            "극한직업",
            "인생은 아름다워"
        ]
    },
    "ESTJ": {
        "books": [
            "자기관리론",
            "원칙"
        ],
        "movies": [
            "미션 임파서블: 데드 레코닝",
            "탑건: 매버릭"
        ]
    },
    "ESFJ": {
        "books": [
            "미드나잇 라이브러리",
            "아주 희미한 빛으로도"
        ],
        "movies": [
            "겨울왕국2",
            "알라딘"
        ]
    },
    "ISTP": {
        "books": [
            "팩트풀니스",
            "사피엔스"
        ],
        "movies": [
            "존 윅 4",
            "분노의 질주"
        ]
    },
    "ISFP": {
        "books": [
            "여행의 이유",
            "참을 수 없는 존재의 가벼움"
        ],
        "movies": [
            "엘리멘탈",
            "너의 이름은"
        ]
    },
    "ESTP": {
        "books": [
            "럭키",
            "김미경의 마흔 수업"
        ],
        "movies": [
            "범죄도시3",
            "베테랑2"
        ]
    },
    "ESFP": {
        "books": [
            "불변의 법칙",
            "1퍼센트 부자의 법칙"
        ],
        "movies": [
            "스즈메의 문단속",
            "인사이드 아웃 2"
        ]
    }
}

# MBTI 선택
selected_mbti = st.selectbox(
    "👇 MBTI를 선택하세요",
    list(mbti_data.keys())
)

# 결과 출력
st.divider()

st.subheader(f"✨ {selected_mbti} 추천 결과")

# 책 추천
st.markdown("## 📚 추천 책")

for book in mbti_data[selected_mbti]["books"]:
    st.markdown(f"- {book}")

st.caption("※ 최근 교보문고 베스트셀러 및 인기 도서를 참고하여 구성")

# 영화 추천
st.markdown("## 🎬 추천 영화")

for movie in mbti_data[selected_mbti]["movies"]:
    st.markdown(f"- {movie}")

st.caption("※ 2020년 이후 CGV 인기 영화 및 관객 반응 참고")

st.success("다른 MBTI도 선택해보세요!")

# 하단 정보
st.markdown("---")
st.write("Made with Streamlit 💙")
