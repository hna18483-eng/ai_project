import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =====================================
# 페이지 설정
# =====================================
st.set_page_config(
    page_title="LG TWINS 선수별 기록표",
    page_icon="⚾",
    layout="wide"
)

# =====================================
# 한글 폰트
# =====================================
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# =====================================
# CSS
# =====================================
st.markdown("""
<style>

.stApp{
    background-color:#FFF8F8;
}

.block-container{
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# 데이터 불러오기
# =====================================
@st.cache_data
def load_data():

    try:
        df = pd.read_csv("kbo.csv", encoding="cp949")
    except:
        df = pd.read_csv("kbo.csv", encoding="euc-kr")

    return df

df = load_data()

# =====================================
# 제목
# =====================================
st.markdown("""
<h1 style='text-align:center;color:#C30452;'>
⚾ LG TWINS 선수별 기록표 ⚾
</h1>

<h4 style='text-align:center;'>
🥎 LG 트윈스 선수 기록 분석 시스템 🥎
</h4>

<hr>
""", unsafe_allow_html=True)

# =====================================
# 선수 선택
# =====================================
players = sorted(df["Name"].unique())

selected_player = st.selectbox(
    "⚾ 선수 선택",
    players
)

player_data = df[df["Name"] == selected_player].iloc[0]

# =====================================
# 기록명 한글 변환
# =====================================
column_korean = {

    "G":"경기수",
    "PA":"타석",
    "AB":"타수",
    "R":"득점",
    "H":"안타",
    "2B":"2루타",
    "3B":"3루타",
    "HR":"홈런",
    "RBI":"타점",
    "SB":"도루",
    "CS":"도루실패",
    "BB":"볼넷",
    "IBB":"고의4구",
    "HBP":"사구",
    "SO":"삼진",

    "AVG":"타율",
    "OBP":"출루율",
    "SLG":"장타율",
    "OPS":"OPS",

    "WAR":"WAR",
    "oWAR":"공격 WAR",
    "dWAR":"수비 WAR"
}

# =====================================
# 숫자형 컬럼 추출
# =====================================
numeric_cols = []

for col in df.columns:

    if col in ["Name", "Pos."]:
        continue

    try:
        float(player_data[col])
        numeric_cols.append(col)
    except:
        pass

x_labels = [
    column_korean.get(col, col)
    for col in numeric_cols
]

y_values = [
    float(player_data[col])
    for col in numeric_cols
]

# =====================================
# 선수 정보
# =====================================
st.markdown(
    f"""
    ### ⚾ 선택 선수 : {selected_player}
    """
)

# =====================================
# 그래프
# =====================================
fig, ax = plt.subplots(figsize=(16, 7))

fig.patch.set_facecolor("#FDECEC")
ax.set_facecolor("#FFF5F5")

ax.plot(
    x_labels,
    y_values,
    color="black",
    marker="o",
    linewidth=3,
    markersize=8
)

ax.set_title(
    f"LG TWINS 선수별 기록표 ({selected_player})",
    fontsize=18,
    fontweight="bold"
)

ax.set_xlabel("기록명")
ax.set_ylabel("기록 수치")

ax.tick_params(
    axis="x",
    rotation=60
)

ax.grid(
    True,
    linestyle="--",
    alpha=0.4
)

plt.tight_layout()

st.pyplot(
    fig,
    use_container_width=True
)

# =====================================
# TOP 5 기록
# =====================================
st.markdown("---")
st.subheader("🏆 주요 기록 TOP 5")

top_df = pd.DataFrame({
    "기록": x_labels,
    "값": y_values
})

top_df = (
    top_df
    .sort_values("값", ascending=False)
    .head(5)
)

cols = st.columns(5)

for i, (_, row) in enumerate(top_df.iterrows()):

    cols[i].metric(
        label=row["기록"],
        value=round(row["값"], 3)
    )

# =====================================
# 전체 기록표
# =====================================
st.markdown("---")
st.subheader("📋 전체 기록")

record_df = pd.DataFrame({
    "기록명": x_labels,
    "기록값": y_values
})

st.dataframe(
    record_df,
    use_container_width=True,
    hide_index=True
)

# =====================================
# 하단
# =====================================
st.markdown("""
<hr>

<div style='text-align:center'>

### ⚾ LG TWINS Baseball Analytics ⚾

🥎 LET'S GO TWINS 🥎

</div>
""")
