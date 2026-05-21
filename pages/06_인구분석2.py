import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# 한글 깨짐 방지
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
# CSV 불러오기
# ---------------------------
df = pd.read_csv("popuiation.csv")

# ---------------------------
# 행정구 컬럼
# ---------------------------
district_col = df.columns[0]

# ---------------------------
# 나이 컬럼 찾기
# ---------------------------
age_columns = []

for col in df.columns:
    if "세" in col:
        age_columns.append(col)

# ---------------------------
# 행정구 선택
# ---------------------------
selected_district = st.selectbox(
    "행정구를 선택하세요",
    df[district_col]
)

# ---------------------------
# 선택 데이터
# ---------------------------
selected_row = df[df[district_col] == selected_district]

# ---------------------------
# 그래프 데이터 준비
# ---------------------------
ages = []
populations = []

for col in age_columns:
    try:
        value = selected_row[col].values[0]

        value = str(value).replace(",", "")
        value = int(float(value))

        ages.append(col)
        populations.append(value)

    except:
        pass

# ---------------------------
# 그래프
# ---------------------------
fig, ax = plt.subplots(figsize=(15, 7))

# 배경색 (연노랑)
fig.patch.set_facecolor('#FFF9DB')
ax.set_facecolor('#FFF9DB')

# 선 색 (연핑크)
ax.plot(
    ages,
    populations,
    color='#FFB6C1',
    linewidth=3,
    marker='o'
)

# 제목
ax.set_title(
    f"{selected_district} 연령별 인구수",
    fontsize=20,
    fontweight='bold'
)

# 축 이름
ax.set_xlabel("나이")
ax.set_ylabel("인구수")

# x축 회전
plt.xticks(rotation=45)

# 격자
ax.grid(alpha=0.3)

# 출력
st.pyplot(fig)
