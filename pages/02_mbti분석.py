import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# 페이지 설정
st.set_page_config(
    page_title="🌍 국가별 MBTI 분석",
    page_icon="🌍",
    layout="wide"
)

# CSS
st.markdown("""
<style>
.main {
    background-color: #f9fbff;
}

h1 {
    color: #ff4fa3;
    text-align: center;
}

.stSelectbox label {
    font-size:18px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# 제목
st.title("🌍 국가별 MBTI 비율 분석")
st.markdown("국가를 선택하면 MBTI 유형 비율을 인터랙티브하게 확인할 수 있습니다.")

# 데이터 불러오기
df = pd.read_csv("countriesMBTI_16types.csv")

# 국가 선택
country = st.selectbox(
    "국가를 선택하세요",
    sorted(df["Country"].unique())
)

# 선택 국가 데이터
selected = df[df["Country"] == country]

# MBTI 컬럼
mbti_cols = [
    'INFJ', 'ISFJ', 'INTP', 'ISFP',
    'ENTP', 'INFP', 'ENTJ', 'ISTP',
    'INTJ', 'ESFP', 'ESTJ', 'ENFP',
    'ESTP', 'ISTJ', 'ENFJ', 'ESFJ'
]

# 데이터 정리
values = selected[mbti_cols].values.flatten()

plot_df = pd.DataFrame({
    "MBTI": mbti_cols,
    "Ratio": values
})

# 최고값 찾기
max_value = plot_df["Ratio"].max()

# 색상 설정
colors = []

for v in plot_df["Ratio"]:
    if v == max_value:
        colors.append("#ff4fa3")  # 핑크
    else:
        colors.append("rgba(135,206,250,0.7)")  # 하늘색

# Plotly 그래프
fig = go.Figure()

fig.add_trace(go.Bar(
    x=plot_df["MBTI"],
    y=plot_df["Ratio"],
    marker=dict(
        color=colors,
        line=dict(color="white", width=1.5)
    ),
    text=[f"{v:.2%}" for v in plot_df["Ratio"]],
    textposition='outside',
    hovertemplate=
        "<b>%{x}</b><br>" +
        "비율: %{y:.2%}<extra></extra>"
))

# 레이아웃
fig.update_layout(
    title=f"📊 {country} MBTI 비율",
    template="plotly_white",
    height=600,
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    font=dict(size=16),
    plot_bgcolor="#ffffff",
    paper_bgcolor="#ffffff",
    hoverlabel=dict(
        bgcolor="white",
        font_size=15
    )
)

# y축 퍼센트 표시
fig.update_yaxes(
    tickformat=".0%"
)

# 출력
st.plotly_chart(fig, use_container_width=True)

# 상위 MBTI
top_mbti = plot_df.sort_values("Ratio", ascending=False).iloc[0]

st.success(
    f"✨ {country}에서 가장 높은 MBTI는 "
    f"**{top_mbti['MBTI']} ({top_mbti['Ratio']:.2%})** 입니다."
)

# 데이터 테이블
with st.expander("📋 데이터 보기"):
    st.dataframe(plot_df, use_container_width=True)

# 평균 비교
st.subheader("🌎 전체 국가 평균과 비교")

avg_df = df[mbti_cols].mean().reset_index()
avg_df.columns = ["MBTI", "Average"]

compare_df = plot_df.merge(avg_df, on="MBTI")

fig2 = px.line(
    compare_df,
    x="MBTI",
    y=["Ratio", "Average"],
    markers=True
)

fig2.update_layout(
    template="plotly_white",
    height=500,
    yaxis_tickformat=".0%",
    legend_title="구분"
)

st.plotly_chart(fig2, use_container_width=True)
