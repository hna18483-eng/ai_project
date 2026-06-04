import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np

# =========================
# 페이지 설정
# =========================
st.set_page_config(
    page_title="LG TWINS 선수별 기록표",
    page_icon="⚾",
    layout="wide"
)

# =========================
# 한글 폰트 설정
# =========================
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# =========================
# 타이틀
# =========================
st.markdown(
    """
    # ⚾ LG TWINS 선수별 기록표 ⚾
    ### 🥎 선수 기록 분석 시스템 🥎
    ---
    """,
    unsafe_allow_html=True
)

# =========================
# 데이터 불러오기
# =========================
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("kbo.csv", encoding="cp949")
    except:
        df = pd.read_csv("kbo.csv", encoding="euc-kr")
    return df

df = load_data()

# =========================
# 선수 선택
# =========================
players = sorted(df["Name"].unique())

selected_player = st.selectbox(
    "⚾ 선수 선택",
    players
)

# =========================
# 선택 선수 데이터
# =========================
player_data = df[df["Name"] == selected_player].iloc[0]

# =========================
# 숫자형 컬럼만 추출
# =========================
numeric_cols = []

for col in df.columns:
    if col in ["Name", "Pos."]:
        continue

    try:
        float(player_data[col])
        numeric_cols.append(col)
    except:
        pass

x = numeric_cols
y = [float(player_data[col]) for col in numeric_cols]

# =========================
# 그래프
# =========================
fig, ax = plt.subplots(figsize=(18, 8))

# 배경 빨강
fig.patch.set_facecolor("red")
ax.set_facecolor("red")

# 선 그래프
ax.plot(
    x,
    y,
    color="black",
    marker="o",
    linewidth=3,
    markersize=8
)

# 제목
ax.set_title(
    f"LG TWINS 선수별 기록표\n({selected_player})",
    fontsize=20,
    fontweight="bold",
    color="white"
)

# 축 글자
ax.tick_params(axis="x", rotation=70, colors="white")
ax.tick_params(axis="y", colors="white")

# 축 테두리
for spine in ax.spines.values():
    spine.set_color("white")

# 그리드
ax.grid(True, linestyle="--", alpha=0.4)

# 축 이름
ax.set_xlabel("기록명", fontsize=13, color="white")
ax.set_ylabel("기록 수치", fontsize=13, color="white")

plt.tight_layout()

st.pyplot(fig, use_container_width=True)

# =========================
# 선수 기록표
# =========================
st.markdown("---")
st.subheader(f"🥎 {selected_player} 상세 기록")

record_df = pd.DataFrame({
    "기록명": x,
    "기록값": y
})

st.dataframe(
    record_df,
    use_container_width=True,
    hide_index=True
)

# =========================
# 하단 꾸미기
# =========================
st.markdown(
    """
    ---
    ### ⚾ 🥎 ⚾ 🥎 ⚾ 🥎 ⚾
    #### LG TWINS Baseball Analytics
    #### ⚾ LET'S GO TWINS ⚾
    """
)
