import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천", page_icon="💼")

st.title("💼 MBTI 기반 진로 추천 프로그램")
st.write("MBTI 유형을 선택하면 추천 진로 2가지와 관련 정보를 알려드립니다.")

# MBTI별 데이터
career_data = {
    "INTJ": [
        {
            "job": "데이터 과학자",
            "major": "컴퓨터공학과, 통계학과",
            "personality": "논리적이고 분석적인 사람",
            "salary": "평균 연봉 약 6,500만원"
        },
        {
            "job": "전략 컨설턴트",
            "major": "경영학과, 경제학과",
            "personality": "계획적이고 문제 해결 능력이 뛰어난 사람",
            "salary": "평균 연봉 약 7,000만원"
        }
    ],
    "INTP": [
        {
            "job": "소프트웨어 개발자",
            "major": "컴퓨터공학과",
            "personality": "창의적이고 호기심이 많은 사람",
            "salary": "평균 연봉 약 5,500만원"
        },
        {
            "job": "연구원",
            "major": "물리학과, 화학과",
            "personality": "탐구심이 강하고 독립적인 사람",
            "salary": "평균 연봉 약 5,800만원"
        }
    ],
    "ENTJ": [
        {
            "job": "기업 CEO",
            "major": "경영학과",
            "personality": "리더십이 강하고 목표 지향적인 사람",
            "salary": "평균 연봉 약 9,000만원"
        },
        {
            "job": "프로젝트 매니저",
            "major": "산업공학과",
            "personality": "조직 관리 능력이 뛰어난 사람",
            "salary": "평균 연봉 약 6,500만원"
        }
    ],
    "ENTP": [
        {
            "job": "마케팅 전문가",
            "major": "광고홍보학과",
            "personality": "아이디어가 많고 도전적인 사람",
            "salary": "평균 연봉 약 5,500만원"
        },
        {
            "job": "창업가",
            "major": "경영학과",
            "personality": "혁신적이고 활동적인 사람",
            "salary": "평균 연봉 약 7,000만원"
        }
    ],
    "INFJ": [
        {
            "job": "심리상담사",
            "major": "심리학과",
            "personality": "공감 능력이 뛰어난 사람",
            "salary": "평균 연봉 약 4,800만원"
        },
        {
            "job": "작가",
            "major": "문예창작과",
            "personality": "감수성이 풍부한 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],
    "INFP": [
        {
            "job": "디자이너",
            "major": "시각디자인학과",
            "personality": "창의적이고 감성적인 사람",
            "salary": "평균 연봉 약 4,700만원"
        },
        {
            "job": "사회복지사",
            "major": "사회복지학과",
            "personality": "따뜻하고 배려심 있는 사람",
            "salary": "평균 연봉 약 4,200만원"
        }
    ],
    "ENFJ": [
        {
            "job": "교사",
            "major": "교육학과",
            "personality": "사람을 이끄는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "인사 담당자",
            "major": "경영학과",
            "personality": "소통 능력이 좋은 사람",
            "salary": "평균 연봉 약 5,300만원"
        }
    ],
    "ENFP": [
        {
            "job": "방송인",
            "major": "미디어커뮤니케이션학과",
            "personality": "에너지가 넘치고 사교적인 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "기획자",
            "major": "경영학과",
            "personality": "창의적이고 자유로운 사람",
            "salary": "평균 연봉 약 5,500만원"
        }
    ],
    "ISTJ": [
        {
            "job": "공무원",
            "major": "행정학과",
            "personality": "책임감이 강하고 성실한 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "회계사",
            "major": "회계학과",
            "personality": "꼼꼼하고 체계적인 사람",
            "salary": "평균 연봉 약 7,000만원"
        }
    ],
    "ISFJ": [
        {
            "job": "간호사",
            "major": "간호학과",
            "personality": "배려심이 많고 책임감 있는 사람",
            "salary": "평균 연봉 약 5,200만원"
        },
        {
            "job": "유치원 교사",
            "major": "유아교육과",
            "personality": "친절하고 인내심 있는 사람",
            "salary": "평균 연봉 약 4,300만원"
        }
    ],
    "ESTJ": [
        {
            "job": "경찰관",
            "major": "경찰행정학과",
            "personality": "원칙을 중요시하는 사람",
            "salary": "평균 연봉 약 5,500만원"
        },
        {
            "job": "은행원",
            "major": "경제학과",
            "personality": "신뢰감 있고 조직적인 사람",
            "salary": "평균 연봉 약 6,000만원"
        }
    ],
    "ESFJ": [
        {
            "job": "승무원",
            "major": "항공서비스학과",
            "personality": "친절하고 사교적인 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "호텔리어",
            "major": "호텔관광학과",
            "personality": "서비스 정신이 뛰어난 사람",
            "salary": "평균 연봉 약 4,800만원"
        }
    ],
    "ISTP": [
        {
            "job": "기계 엔지니어",
            "major": "기계공학과",
            "personality": "실용적이고 문제 해결을 좋아하는 사람",
            "salary": "평균 연봉 약 6,000만원"
        },
        {
            "job": "파일럿",
            "major": "항공운항학과",
            "personality": "침착하고 집중력이 높은 사람",
            "salary": "평균 연봉 약 8,000만원"
        }
    ],
    "ISFP": [
        {
            "job": "플로리스트",
            "major": "원예학과",
            "personality": "감각적이고 섬세한 사람",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "job": "사진작가",
            "major": "사진학과",
            "personality": "예술 감각이 뛰어난 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],
    "ESTP": [
        {
            "job": "영업 전문가",
            "major": "경영학과",
            "personality": "활동적이고 도전적인 사람",
            "salary": "평균 연봉 약 6,000만원"
        },
        {
            "job": "스포츠 코치",
            "major": "체육학과",
            "personality": "에너지가 넘치고 리더십 있는 사람",
            "salary": "평균 연봉 약 4,800만원"
        }
    ],
    "ESFP": [
        {
            "job": "배우",
            "major": "연극영화과",
            "personality": "표현력이 풍부한 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "이벤트 플래너",
            "major": "관광경영학과",
            "personality": "사람들과 어울리기 좋아하는 사람",
            "salary": "평균 연봉 약 4,700만원"
        }
    ]
}

# 선택 박스
selected_mbti = st.selectbox(
    "MBTI 유형을 선택하세요",
    list(career_data.keys())
)

# 결과 출력
st.subheader(f"✨ {selected_mbti} 추천 진로")

for idx, career in enumerate(career_data[selected_mbti], start=1):
    st.markdown(f"""
    ### {idx}. {career['job']}
    - 📚 적합 학과: {career['major']}
    - 😊 적합한 성격: {career['personality']}
    - 💰 평균 연봉: {career['salary']}
    """)

st.success("원하는 MBTI를 선택해서 진로를 확인해보세요!")
