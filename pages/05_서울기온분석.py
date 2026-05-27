# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# -----------------------------
# 한글 폰트 설정
# -----------------------------
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# -----------------------------
# 데이터 불러오기
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv('seoul.csv', encoding='cp949')

    df['날짜'] = pd.to_datetime(df['날짜'])

    df['월'] = df['날짜'].dt.month
    df['일'] = df['날짜'].dt.day
    df['연도'] = df['날짜'].dt.year

    return df

df = load_data()

# -----------------------------
# 제목
# -----------------------------
st.title("서울 기온 분석")

st.write("월과 일을 선택하면 연도별 최고/최저 기온 변화를 볼 수 있습니다.")

# -----------------------------
# 월 / 일 선택
# -----------------------------
month = st.selectbox("월 선택", list(range(1, 13)))

day = st.selectbox("일 선택", list(range(1, 32)))

# -----------------------------
# 선택 날짜 데이터
# -----------------------------
filtered = df[(df['월'] == month) & (df['일'] == day)]

# 결측 제거
filtered = filtered.dropna(subset=['최고기온(℃)', '최저기온(℃)'])

# -----------------------------
# 그래프 출력
# -----------------------------
if len(filtered) > 0:

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(
        filtered['연도'],
        filtered['최고기온(℃)'],
        color='pink',
        label='최고기온',
        linewidth=2
    )

    ax.plot(
        filtered['연도'],
        filtered['최저기온(℃)'],
        color='skyblue',
        label='최저기온',
        linewidth=2
    )

    ax.set_title(f'{month}월 {day}일 연도별 기온 변화')

    ax.set_xlabel('연도')
    ax.set_ylabel('기온(℃)')

    ax.legend()

    ax.grid(True)

    st.pyplot(fig)

else:
    st.warning("해당 날짜의 데이터가 없습니다.")
