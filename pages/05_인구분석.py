import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# ---------------------------
# 한글 폰트 설정
# ---------------------------
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# ---------------------------
# 페이지 설정
# ---------------------------
st.set_page_config(
    page_title="서울시 행정구별 인구수",
    layout="wide"
)

# ---------------------------
# 제목
# ---------------------------
st.title("서울시 행정구별 인구수")

# ---------------------------
# 데이터 불러오기
# ---------------------------
df = pd.read_csv("popuiation.csv", encoding="utf-8")

# ---------------------------
# 행정구 컬럼 찾기
# ---------------------------
district_col = df.columns[0]

# ---------------------------
# 나이 관련 컬럼 찾기
# ---------------------------
age_columns = []

for col in df.columns:
    if "세" in col or "연령" in col:
        age_columns.append(col)

# ---------------------------
# 행정구 선택
# ---------------------------
districts = df[district_col].tolist()

selected_district = st.selectbox(
    "행정구를 선택하세요",
    districts
)

# ---------------------------
# 선택 데이터 추출
# ---------------------------
selected_data = df[df[district_col] == selected_district]

# ---------------------------
# 나이 / 인구 데이터 정리
# ---------------------------
ages = []
population = []

for col in age_columns:
    try:
        value = selected_data[col].values[0]

        # 숫자형 변환
        value = str(value).replace(",", "")
        value = float(value)

        ages.append(col)
        population.append(value)

    except:
        pass

# ---------------------------
# 그래프 생성
# ---------------------------
fig, ax = plt.subplots(figsize=(14, 7))

# 배경색
fig.patch.set_facecolor('#FFF9DB')
ax.set_facecolor('#FFF9DB')

# 꺾은선 그래프
ax.plot(
    ages,
    population,
    color='#FFB6C1',
    linewidth=3,
    marker='o',
    markersize=6
)

# 그래프 제목
ax.set_title(
    f"{selected_district} 연령별 인구수",
    fontsize=20,
    fontweight='bold'
)

# 축 제목
ax.set_xlabel("나이", fontsize=14)
ax.set_ylabel("인구수", fontsize=14)

# x축 글자 회전
plt.xticks(rotation=45)

# 격자
ax.grid(alpha=0.3)

# Streamlit 출력
st.pyplot(fig)
