import streamlit as st
import pandas as pd
import plotly.express as px

# CSS로 제목과 콘텐츠를 가운데 정렬
st.markdown(
    """
    <style>
    .center-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 사이드바: 모델 선택
model_option = st.sidebar.selectbox(
    "model",
    ("select", "model1", "model2", "model3", "자세히")
)

# 사이드바: 지표 선택
stat_option = st.sidebar.selectbox(
    "stat",
    ("select", "환율", "금 시세", "유가", "유류세")
)

# 페이지 콘텐츠
st.markdown('<div class="center-content">', unsafe_allow_html=True)

# 제목
st.title("ㅇㅇ은 주유하기 좋은 날")

# 메인 설명 텍스트
st.write("구체적인 지표를 알고 싶으면 스크롤해주세요!")

# 그래프1: 증감율 (임시 라인그래프)
data = pd.DataFrame({
    "날짜": ["2023-01-01", "2023-01-02", "2023-01-03"],
    "증감율": [1.2, -0.5, 2.3]
})
fig1 = px.line(data, x="날짜", y="증감율", title="증감율")
st.plotly_chart(fig1)

# 그래프2: 휘발유가 (소비자가; 임시 라인그래프)
data2 = pd.DataFrame({
    "날짜": ["2023-01-01", "2023-01-02", "2023-01-03"],
    "휘발유가": [1600, 1620, 1580]
})
fig2 = px.line(data2, x="날짜", y="휘발유가", title="휘발유가")
st.plotly_chart(fig2)

st.markdown('</div>', unsafe_allow_html=True)

# 조건부로 콘텐츠 렌더링
if model_option != "select" or stat_option != "select":
    if model_option != "select":
        st.subheader(f"selected model: {model_option}")
        if model_option == "model1":
            st.write("여기에는 model1에 대한 내용을 작성합니다.")
        elif model_option == "model2":
            st.write("여기에는 model2에 대한 내용을 작성합니다.")
        elif model_option == "model3":
            st.write("여기에는 model3에 대한 내용을 작성합니다.")
        else:
            st.write("여기에는 자세히 보기와 관련된 내용을 작성합니다.")

    if stat_option != "select":
        st.subheader(f"selected stat: {stat_option}")
        
        if stat_option == "환율":
            st.write("환율 지표에 대한 내용을 작성합니다.")
            # External data loading
            url = "https://raw.githubusercontent.com/Waterrrrrit/2025-01-TheFree/refs/heads/main/%ED%99%98%EC%9C%A8_%EC%B5%9C%EC%A2%85.csv"
            try:
                data = pd.read_csv(url)

                # Convert the '일자' column to datetime format and sort the data by date
                data['일자'] = pd.to_datetime(data['일자'])
                data = data.sort_values(by='일자')

                # Plot the data using Plotly Express
                fig = px.line(data, x='일자', y='원/달러', title='원/달러 (2020-2023)')
                st.plotly_chart(fig)

            except Exception as e:
                st.write("데이터를 불러오는 중 문제가 발생했습니다:", str(e))
        elif stat_option == "금 시세":
            st.write("과거의 금 시세 변동을 확인합니다.")

            # External data loading
            url = "https://raw.githubusercontent.com/Waterrrrrit/2025-01-TheFree/refs/heads/main/iG_2020-2023_filled.csv"
            try:
                data = pd.read_csv(url)

                # Convert the '일자' column to datetime format and sort the data by date
                data['일자'] = pd.to_datetime(data['일자'])
                data = data.sort_values(by='일자')

                # Plot the data using Plotly Express
                fig = px.line(data, x='일자', y='원/g_시가', title='원/g_시가 (2020-2023)')
                st.plotly_chart(fig)

            except Exception as e:
                st.write("데이터를 불러오는 중 문제가 발생했습니다:", str(e))

        elif stat_option == "유가":
            st.write("과거 유가 변동을 확인합니다.")
            # External data loading
            url = "https://raw.githubusercontent.com/Waterrrrrit/2025-01-TheFree/refs/heads/main/%EC%9C%A0%EA%B0%80file2.csv"
            try:
                data = pd.read_csv(url)

                # Convert the '일자' column to datetime format and sort the data by date
                data['일자'] = pd.to_datetime(data['일자'])
                data = data.sort_values(by='일자')

                # Plot the data using Plotly Express
                fig = px.line(data, x='일자', y='달러/배럴', title='달러/배럴 (2020-2023)')
                st.plotly_chart(fig)

            except Exception as e:
                st.write("데이터를 불러오는 중 문제가 발생했습니다:", str(e))

        else:
            st.write("과거 유류세 변동을 확인합니다.")
            # External data loading
            url = "https://raw.githubusercontent.com/Waterrrrrit/2025-01-TheFree/refs/heads/main/%EC%9C%A0%EB%A5%98%EC%84%B8_%EC%B5%9C%EC%A2%85.csv"
            try:
                data = pd.read_csv(url)

                # Convert the '일자' column to datetime format and sort the data by date
                data['일자'] = pd.to_datetime(data['일자'])
                data = data.sort_values(by='일자')

                # Plot the data using Plotly Express
                fig = px.line(data, x='일자', y='원/리터', title='원/리터 (2020-2023)')
                st.plotly_chart(fig)

            except Exception as e:
                st.write("데이터를 불러오는 중 문제가 발생했습니다:", str(e))

            
else:
    st.write("사이드바에서 비교 모델 또는 지표를 선택해주세요.")

# sub 설명 텍스트
st.write("출처:")
