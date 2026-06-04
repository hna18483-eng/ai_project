import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================
# 페이지 설정
# =====================================
st.set_page_config(
    page_title="LG TWINS 선수별 기록표",
    page_icon="⚾",
    layout="wide"
)

# =====================================
# CSS
# =====================================
st.markdown("""
<style>

.stApp{
    background-color:#FFF8F8;
}

h1,h2,h3,h4{
    text-align:center;
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
        try:
            df = pd.read_csv("kbo.csv", encoding="euc-kr")
        except:
            df = pd.read_csv("kbo.csv")

    return df

df = load_data()

# =====================================
# 제목
# =====================================
st.markdown("""
# ⚾ LG TWINS 선수별 기록표 ⚾

### 🥎 LG 트윈스 선수 기록 분석 시스템 🥎

---
""")

# =====================================
# 선수 선택
# =====================================
players = sorted(df["Name"].dropna().unique())

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
    "dWAR":"수비 WAR",

    "wRC+":"조정득점생산력",
    "wOBA":"가중출루율",
    "BABIP":"인플레이타율",
    "ISO":"순장타율"
}

# =====================================
# 숫자 컬럼 추출
# =====================================
numeric_cols = []

for col in df.columns:

    if col in ["Name", "Pos."]:
        continue

    try:
        value = pd.to_numeric(player_data[col])

        if pd.notnull(value):
            numeric_cols.append(col)

    except:
        continue

# =====================================
# 데이터 생성
# =====================================
graph_df = pd.DataFrame({
    "기록명":[column_korean.get(col, col) for col in numeric_cols],
    "기록값":[float(player_data[col]) for col in numeric_cols]
})

# =====================================
# 선수 정보
# =====================================
st.markdown(f"""
## ⚾ {selected_player}
""")

# =====================================
# Plotly 그래프
# =====================================
fig = px.line(
    graph_df,
    x="기록명",
    y="기록값",
    markers=True,
    title=f"LG TWINS 선수별 기록표 ({selected_player})"
)

fig.update_traces(
    line=dict(
        color="black",
        width=4
    ),
    marker=dict(
        size=9,
        color="black"
    )
)

fig.update_layout(

    paper_bgcolor="#FDECEC",
    plot_bgcolor="#FFF5F5",

    font=dict(
        size=14
    ),

    title=dict(
        x=0.5
    ),

    xaxis=dict(
        tickangle=-45
    ),

    height=650
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# TOP5 기록
# =====================================
st.markdown("---")

st.subheader("🏆 주요 기록 TOP 5")

top_df = graph_df.sort_values(
    by="기록값",
    ascending=False
).head(5)

cols = st.columns(5)

for i, (_, row) in enumerate(top_df.iterrows()):

    cols[i].metric(
        label=row["기록명"],
        value=round(row["기록값"], 3)
    )

# =====================================
# 전체 기록표
# =====================================
st.markdown("---")

st.subheader("📋 전체 기록")

st.dataframe(
    graph_df,
    use_container_width=True,
    hide_index=True
)

# =====================================
# 하단 꾸미기
# =====================================
st.markdown("""
---

# ⚾ 🥎 ⚾ 🥎 ⚾

### LG TWINS Baseball Analytics

### LET'S GO TWINS

⚾ 🥎 ⚾ 🥎 ⚾

---
""")
