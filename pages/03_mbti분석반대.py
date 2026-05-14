import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# =========================
# 페이지 설정
# =========================
st.set_page_config(
    page_title="🌍 MBTI 국가 순위",
    page_icon="🌍",
    layout="wide"
)

# =========================
# CSS 스타일
# =========================
st.markdown("""
<style>

.main {
    background-color: #f9fbff;
}

h1 {
    color: #ff4fa3;
    text-align: center;
    font-weight: 800;
}

.stSelectbox label {
    font-size:18px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# =========================
# 제목
# =========================
st.title("🌍 MBTI별 국가 순위 TOP10")

st.markdown(
    """
    원하는 MBTI를 선택하면  
    해당 유형 비율이 높은 국가 TOP10을 확인할 수 있습니다.
    """
)

# =========================
# 데이터 불러오기
# =========================
df = pd.read_csv("countriesMBTI_16types.csv")

# =========================
# MBTI 컬럼
# =========================
mbti_cols = [
    'INFJ', 'ISFJ', 'INTP', 'ISFP',
    'ENTP', 'INFP', 'ENTJ', 'ISTP',
    'INTJ', 'ESFP', 'ESTJ', 'ENFP',
    'ESTP', 'ISTJ', 'ENFJ', 'ESFJ'
]

# =========================
# MBTI 선택
# =========================
selected_mbti = st.selectbox(
    "🧠 MBTI를 선택하세요",
    mbti_cols
)

# =========================
# 선택 MBTI 기준 정렬
# =========================
rank_df = df[["Country", selected_mbti]].sort_values(
    by=selected_mbti,
    ascending=False
)

# 컬럼명 변경
rank_df.columns = ["Country", "Ratio"]

# TOP10
rank_df = rank_df.head(10)

# =========================
# 색상 설정
# =========================
max_value = rank_df["Ratio"].max()

colors = []

for value in rank_df["Ratio"]:

    # 1등 핑크
    if value == max_value:
        colors.append("#ff4fa3")

    # 나머지 하늘색 그라데이션 느낌
    else:
        colors.append("rgba(135,206,250,0.75)")

# =========================
# Plotly 그래프
# =========================
fig = go.Figure()

fig.add_trace(go.Bar(

    x=rank_df["Ratio"],
    y=rank_df["Country"],

    orientation='h',

    marker=dict(
        color=colors,

        line=dict(
            color="white",
            width=1.5
        )
    ),

    text=[
        f"{v:.2%}" for v in rank_df["Ratio"]
    ],

    textposition='outside',

    hovertemplate=
        "<b>%{y}</b><br>" +
        "비율: %{x:.2%}<extra></extra>"
))

# =========================
# 그래프 레이아웃
# =========================
fig.update_layout(

    title=f"🏆 {selected_mbti} 국가 순위 TOP10",

    template="plotly_white",

    height=700,

    xaxis_title="비율",
    yaxis_title="국가",

    font=dict(
        size=16
    ),

    plot_bgcolor="#ffffff",
    paper_bgcolor="#ffffff",

    hoverlabel=dict(
        bgcolor="white",
        font_size=15
    )
)

# 퍼센트 표시
fig.update_xaxes(
    tickformat=".0%"
)

# 높은 순이 위로 오게
fig.update_yaxes(
    autorange="reversed"
)

# =========================
# 그래프 출력
# =========================
st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================
# 1등 국가 출력
# =========================
top_country = rank_df.iloc[0]

st.success(
    f"""
    ✨ {selected_mbti} 비율이 가장 높은 국가는  
    **{top_country['Country']} ({top_country['Ratio']:.2%})**
    입니다.
    """
)

# =========================
# 데이터 테이블
# =========================
with st.expander("📋 TOP10 데이터 보기"):

    show_df = rank_df.copy()

    show_df["Ratio"] = (
        show_df["Ratio"] * 100
    ).round(2).astype(str) + "%"

    st.dataframe(
        show_df,
        use_container_width=True
    )

# =========================
# 푸터
# =========================
st.markdown("---")

st.caption("Made with ❤️ using Streamlit & Plotly")
