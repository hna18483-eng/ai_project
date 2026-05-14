import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# ==================================================
# 페이지 설정
# ==================================================
st.set_page_config(
    page_title="🌍 MBTI 국가 분석",
    page_icon="🌍",
    layout="wide"
)

# ==================================================
# CSS 스타일
# ==================================================
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

.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# 제목
# ==================================================
st.title("🌍 MBTI 국가 분석 대시보드")

st.markdown("""
국가별 MBTI 비율과  
MBTI별 국가 순위를 동시에 확인할 수 있습니다.
""")

# ==================================================
# 데이터 불러오기
# ==================================================
df = pd.read_csv("countriesMBTI_16types.csv")

# ==================================================
# MBTI 컬럼
# ==================================================
mbti_cols = [
    'INFJ', 'ISFJ', 'INTP', 'ISFP',
    'ENTP', 'INFP', 'ENTJ', 'ISTP',
    'INTJ', 'ESFP', 'ESTJ', 'ENFP',
    'ESTP', 'ISTJ', 'ENFJ', 'ESFJ'
]

# ==================================================
# 화면 반반 나누기
# ==================================================
left_col, right_col = st.columns(2)

# ==================================================
# 왼쪽 화면
# 국가별 MBTI 분석
# ==================================================
with left_col:

    st.subheader("🌎 국가별 MBTI 비율")

    # 국가 선택
    country = st.selectbox(
        "국가를 선택하세요",
        sorted(df["Country"].unique())
    )

    # 선택 데이터
    selected = df[df["Country"] == country]

    values = selected[mbti_cols].values.flatten()

    plot_df = pd.DataFrame({
        "MBTI": mbti_cols,
        "Ratio": values
    })

    # 최고값
    max_value = plot_df["Ratio"].max()

    # 색상 설정
    colors = []

    for value in plot_df["Ratio"]:

        # 1등 핑크
        if value == max_value:
            colors.append("#ff4fa3")

        # 나머지 하늘색
        else:
            colors.append("rgba(135,206,250,0.75)")

    # Plotly 그래프
    fig1 = go.Figure()

    fig1.add_trace(go.Bar(

        x=plot_df["MBTI"],
        y=plot_df["Ratio"],

        marker=dict(
            color=colors,

            line=dict(
                color="white",
                width=1.5
            )
        ),

        text=[
            f"{v:.2%}" for v in plot_df["Ratio"]
        ],

        textposition='outside',

        hovertemplate=
            "<b>%{x}</b><br>" +
            "비율: %{y:.2%}<extra></extra>"
    ))

    # 레이아웃
    fig1.update_layout(

        title=f"📊 {country} MBTI 비율",

        template="plotly_white",

        height=550,

        xaxis_title="MBTI 유형",
        yaxis_title="비율",

        font=dict(size=14),

        plot_bgcolor="#ffffff",
        paper_bgcolor="#ffffff"
    )

    # 퍼센트 표시
    fig1.update_yaxes(
        tickformat=".0%"
    )

    # 그래프 출력
    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # 최고 MBTI
    top_mbti = plot_df.sort_values(
        "Ratio",
        ascending=False
    ).iloc[0]

    st.success(
        f"""
        ✨ {country}에서 가장 높은 MBTI는  
        **{top_mbti['MBTI']} ({top_mbti['Ratio']:.2%})**
        입니다.
        """
    )

# ==================================================
# 오른쪽 화면
# MBTI별 국가 순위
# ==================================================
with right_col:

    st.subheader("🏆 MBTI별 국가 순위 TOP10")

    # MBTI 선택
    selected_mbti = st.selectbox(
        "MBTI를 선택하세요",
        mbti_cols
    )

    # 정렬
    rank_df = df[["Country", selected_mbti]].sort_values(
        by=selected_mbti,
        ascending=False
    )

    rank_df.columns = ["Country", "Ratio"]

    # TOP10
    rank_df = rank_df.head(10)

    # 최고값
    max_value = rank_df["Ratio"].max()

    # 색상 설정
    colors = []

    for value in rank_df["Ratio"]:

        # 1등 핑크
        if value == max_value:
            colors.append("#ff4fa3")

        # 나머지 하늘색
        else:
            colors.append("rgba(135,206,250,0.75)")

    # Plotly 그래프
    fig2 = go.Figure()

    fig2.add_trace(go.Bar(

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

    # 레이아웃
    fig2.update_layout(

        title=f"🏆 {selected_mbti} 국가 순위 TOP10",

        template="plotly_white",

        height=550,

        xaxis_title="비율",
        yaxis_title="국가",

        font=dict(size=14),

        plot_bgcolor="#ffffff",
        paper_bgcolor="#ffffff"
    )

    # 퍼센트 표시
    fig2.update_xaxes(
        tickformat=".0%"
    )

    # 높은 순이 위로
    fig2.update_yaxes(
        autorange="reversed"
    )

    # 그래프 출력
    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # 1등 국가
    top_country = rank_df.iloc[0]

    st.success(
        f"""
        ✨ {selected_mbti} 비율이 가장 높은 국가는  
        **{top_country['Country']} ({top_country['Ratio']:.2%})**
        입니다.
        """
    )

# ==================================================
# 푸터
# ==================================================
st.markdown("---")

st.caption("Made with ❤️ using Streamlit & Plotly")
