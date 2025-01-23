import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import pytz

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
    ("select", "model1", "model2", "model3", "model4")
)

# 사이드바: 지표 선택
stat_option = st.sidebar.selectbox(
    "stat",
    ("select", "환율", "금 시세", "국제 유가", "유류세")
)
# 사이드바: 하단 이미지
image_path = "https://github.com/Waterrrrrit/2025-01-TheFree/blob/main/side_bar_2.png?raw=true"
st.sidebar.markdown("<br><br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)  
st.sidebar.image(image_path, use_container_width=True)  
st.sidebar.markdown(
    "<span style='color:#ced4da; font-size: 14px;'>  본 서비스는 단순 참고용이며, 모든 결정의 책임은 모두 이용자 본인에게 있다는 점을 유의하십시오.</span>", 
    unsafe_allow_html=True
)
# 페이지 콘텐츠
st.markdown('<div class="center-content">', unsafe_allow_html=True)

# 제목
st.markdown("""
<div style='font-size:50px;'>  <!-- 전체 폰트 크기 설정 -->
    <span style='color:#008d62; font-weight:bold; font-size:60px;'>01월 25일</span>이 주유하기 좋은 날!
</div>
""", unsafe_allow_html=True)

# 메인 설명 텍스트
korea_timezone = pytz.timezone("Asia/Seoul")
current_date = datetime.now(korea_timezone).strftime("%Y년 %m월 %d일")  # 날짜 형식 지정
st.markdown(f"""
<div style='text-align: center; font-size: 15px; color:#ced4da;'>
    <span style='font-weight:500;'>오늘은 {current_date} 입니다</span>
</div>
""", unsafe_allow_html=True)

st.divider()
# 그래프1: 증감율 (임시 라인그래프)
st.markdown("""
            <div style='text-align: center; color:#008d62; font-size: 25px;'>
            <span style='color:#008d62 font-size: 40px; font-weight:500;'>증감율
            </div>
            """, unsafe_allow_html=True)
data = pd.DataFrame({
    "날짜": ["2023-01-01", "2023-01-02", "2023-01-03"],
    "증감율": [1.2, -0.5, 2.3]
})
fig1 = px.line(data, x="날짜", y="증감율")
st.plotly_chart(fig1)

# 그래프2: 휘발유가 (소비자가; 임시 라인그래프)
st.markdown("""
            <div style='text-align: center; color:#008d62; font-size: 25px;'>
            <span style='color:#008d62 font-size: 40px; font-weight:500;'>휘발유가
            </div>
            """, unsafe_allow_html=True)
data2 = pd.DataFrame({
    "날짜": ["2023-01-01", "2023-01-02", "2023-01-03"],
    "휘발유가": [1600, 1620, 1580]
})
fig2 = px.line(data2, x="날짜", y="휘발유가")
st.plotly_chart(fig2)
# sub 설명 텍스트

st.divider()
st.markdown('</div>', unsafe_allow_html=True)

# 조건부로 콘텐츠 렌더링
if model_option != "select" or stat_option != "select":
    if model_option != "select":
        st.markdown(f"""
            <div style='color:#808080 font-size: 30px;'>
            <span style='font-weight:200;'>selected model: {model_option}
            </div>
            """, unsafe_allow_html=True)
        
        if model_option == "model1":
            image_url = "https://github.com/Waterrrrrit/2025-01-TheFree/blob/main/25-1_proj_model1_graph.png?raw=true"
            image_url2 = "https://github.com/Waterrrrrit/2025-01-TheFree/blob/main/25-1_proj_model1_Nscore.png?raw=true"
            st.markdown("""
            <div style='text-align: center; font-size: 30px;'>
            <span style='font-weight:500;'>일변수 선형회귀 모델
            </div>
            """, unsafe_allow_html=True)
            
            st.image(image_url, caption="원-달러 환율과 휘발유 가격", use_container_width=True)
            st.markdown("본 알고리즘은 **환율** 데이터를 활용하여 국내 유통 휘발유 가격을 예측하기 위해 설계되었습니다.")
            st.write("단일 변수 선형 회귀 분석 기법을 사용하여 원-달러 환율과 휘발유 가격 간의 상관관계를 분석하였으며, 이는 간결성과 예측 가능성을 목표로 한 초기 모델링 접근법입니다.")  
            st.divider()
            st.subheader("성능 개요/일변수 선형회귀 모델")
            st.markdown("-**예측 정밀도**: 실제 휘발유 가격(1804원)과의 비교에서 0.5% 내외의 오차를 보이며, 실용적인 수준의 예측 정밀도를 달성")
            st.markdown("-**결정계수(R²)**: 0.218로, 데이터 간 상관성이 낮아 신뢰성 확보는 미흡")
            st.image(image_url2, caption="일변수 선형회귀 모델 결정 계수", use_container_width=True)
            st.divider()
            st.subheader("주요 특장점/일변수 선형회귀 모델")
            st.markdown("-**단순성**: 단일 변수만을 활용한 간결한 구조로, 신속한 분석 가능")
            st.markdown("-**실제 데이터와의 오차 최소화**: 초기 분석에서 0.5% 내외의 오차로 실제 가격에 근접한 예측 달성")       
            st.divider()
            st.markdown("개선 방향")
            st.write("현재 낮은 R² 값은 복합적인 외부 요인(원유 가격, 세금 정책, 국제 정세 등)이 휘발유 가격 형성에 영향을 미친다는 점을 시사합니다. 이를 해결하기 위해 다중 변수 회귀분석 또는 비선형 모델링 접근을 통해 예측 정확도와 신뢰도를 개선할 계획입니다.")   
            st.divider()
            st.divider()
            
            
        elif model_option == "model2":
            image_url3 = "https://github.com/Waterrrrrit/2025-01-TheFree/blob/main/25-1_proj_model2_graph.png?raw=true"
            image_url4 = "https://github.com/Waterrrrrit/2025-01-TheFree/blob/main/25-1_proj_model2_Rscore.png?raw=true"
            st.markdown("""
            <div style='text-align: center; font-size: 30px;'>
            <span style='font-weight:500;'>이변수 선형회귀 모델
            </div>
            """, unsafe_allow_html=True)
            st.image(image_url3, caption="환율과 국제 유가, 그리고 휘발유 가격", use_container_width=True)
            st.markdown("본 모델은 **환율뿐만 아니라 브렌트유 가격을 추가 변수로 사용**하여, 휘발유 가격 예측의 정밀도를 높이기 위해 설계되었습니다.")
            st.write("이는 단일 변수 모델의 한계를 극복하고자 변수 간 상호작용을 반영한 다중 변수 선형 회귀 분석 기법을 도입한 결과입니다.")  
            st.divider()
            st.subheader("성능 개요/2변수 선형회귀 모델")
            st.markdown("-**예측 정밀도**: 실제 휘발유 가격(1804원)과의 비교에서 약 16.5% 오차 발생")
            st.markdown("-**결정계수(R²)**: 0.213으로, 이전 모델(0.218)보다 낮은 결과")
            st.image(image_url4, caption="2변수 선형회귀 모델 결정 계수", use_container_width=True)
            st.divider()
            st.subheader("주요 분석")
            st.markdown("-**두 변수 사용**: 원-달러 환율과 브렌트유 선물 거래 가격을 독립 변수로 설정")
            st.markdown("-**오차 확대**: 실제 가격과의 오차가 커져 성능 향상을 이루지 못함")    
            st.markdown("-**신뢰 수준 부족**:  R² 값이 유의미한 상관성을 입증하기에 미흡")
            st.divider()
            st.subheader("개선 방향")
            st.markdown("변수 추가를 통해 모델을 개선할 계획입니다. 휘발유 가격 형성에는 복합적인 요인이 작용하므로, 원유 가격, 생산 및 유통 비용, 세금 정책, 국제 정세 등의 변수를 추가적으로 고려할 예정입니다.")
            st.divider()
            st.divider()

        elif model_option == "model3":
            image_url5 = "https://github.com/Waterrrrrit/2025-01-TheFree/blob/main/25-1_proj_model3_graph.png?raw=true"
            image_url6 = "https://github.com/Waterrrrrit/2025-01-TheFree/blob/main/25-1_proj_model3_Rscore.png?raw=true"
            st.markdown("""
            <div style='text-align: center; font-size: 30px;'>
            <span style='font-weight:500;'>4변수 선형회귀 모델
            </div>
            """, unsafe_allow_html=True)
            st.image(image_url5, caption="환율, 금 시세, 유류세, 브렌트유 가격", use_container_width=True)
            st.markdown("본 모델은 **총 4개의 변수(환율, 금 시세, 유류세, 브렌트유 가격)**를 활용하여 휘발유 가격 예측의 정밀성을 대폭 향상시키기 위해 설계되었습니다.")
            st.write("이는 이전 세대 모델에서 나타난 낮은 상관성과 예측 오차를 해결하기 위한 주요 발전 단계로, 고도화된 다중 변수 선형 회귀 기법을 도입하였습니다.")  
            st.divider()
            st.subheader("성능 개요/4변수 선형회귀 모델")
            st.markdown("-**높은 예측 정확도**: 실제 휘발유 가격(1804원)과의 오차가 0.1%에 불과")
            st.markdown("-**결정계수(R²)**: 0.88로 대폭 상승, 변수 간 상관성이 유의미하게 입증됨")
            st.markdown("-**평균 제곱 오차(MSE)**: 0.88로 대폭 상승, 변수 간 상관성이 유의미하게 입증됨")
            st.image(image_url6, caption="4변수 선형회귀 모델 결정 계수", use_container_width=True)
            st.divider()
            st.subheader("주요 분석/4변수 선형회귀 모델")
            st.markdown("-**변수 확장**: 4개의 독립 변수를 도입하여 휘발유 가격 형성에 영향을 미치는 다양한 외부 요인을 반영")
            st.markdown("-**정확도와 신뢰성 강화**: R² 값이 신뢰할 만한 수준에 도달, 예측 모델로서의 활용 가능성을 입증")    
            st.markdown("-**복잡도 증가**:  변수 추가로 복잡성이 증가했으나, 이는 성능 향상을 위한 필연적 결과로 해석")        
            st.divider()
            st.subheader("개선 방향")
            st.markdown("모델의 우수한 성능에도 불구하고, 평균 제곱 오차의 증가를 고려해 추가 최적화를 진행할 계획입니다. 변수 간 다중공선성 문제를 점검하고, 비선형 회귀 또는 머신러닝 알고리즘(예: LSTM, GCR)을 도입하여 성능을 더욱 개선할 예정입니다.")
            st.divider()
            st.divider()
            
        else:
            st.markdown("""
            <div style='text-align: center; font-size: 30px;'>
            <span style='font-weight:500;'>4변수 딥러닝 모델
            </div>
            """, unsafe_allow_html=True)
            image_url7 = "https://github.com/Waterrrrrit/2025-01-TheFree/blob/main/25-1_proj_model4_graph.png?raw=true"
            image_url8 = "https://github.com/Waterrrrrit/2025-01-TheFree/blob/main/25-1_proj_model4_Rscore.png?raw=true"
            st.image(image_url7, caption="환율, 금 시세, 유류세, 브렌트유 가격_딥러닝", use_container_width=True)
            st.markdown("본 단계에서는 **4개의 변수를 기반으로 은닉층을 포함한 다층 퍼셉트론(MLP) 구조를 채택**하여 선형 모델 이상의 예측 성능을 달성하고자 하였습니다.")
            st.divider()
            st.subheader("성능 개요/4변수 딥러닝 모델")
            st.markdown("-**오차 감소**: 실제 휘발유 가격(1804원)과의 오차가 0.1%에 불과")
            st.markdown("-**오버피팅**: 학습 데이터 부족으로 인해 모델이 훈련 데이터에 과적합되고, 일반화 성능이 저하")
            st.markdown("-**하이퍼 파라미터 한계**: 적절한 가중치 및 구조 설정 실패")
            st.image(image_url8, caption="4변수 딥러닝 모델 상관 계수", use_container_width=True)
            st.divider()
            st.subheader("주요 분석/4변수 딥러닝 모델")
            st.markdown("-**선형 관계의 명확성**: 변수들 간의 선형적 특성이 뚜렷해, 복잡한 딥러닝 모델의 필요성 부족")
            st.markdown("-**기존선형 모델 유지**: 딥러닝 모델의 복잡도와 성능을 비교한 결과, 선형 회귀 모델 유지가 적합")
            st.divider()
            st.subheader("개선 방향")
            st.markdown("-**앙상블 모델 개발**: 선형 모델과 딥러닝 모델의 장점을 통합한 앙상블 모델 설계")
            st.markdown("-**데이터 확장 및 튜닝 개선**: 학습 데이터 확보 및 하이퍼파라미터 최적화를 통해 딥러닝 모델의 성능 재검토")
            st.divider()
            st.divider()

    if stat_option != "select":
        st.markdown(f"""
            <div style='color:#808080 font-size: 30px;'>
            <span style='font-weight:200;'>selected stat: {stat_option}
            </div>
            """, unsafe_allow_html=True)
        
        if stat_option == "환율":
            # External data loading
            url = "https://raw.githubusercontent.com/Waterrrrrit/2025-01-TheFree/refs/heads/main/%ED%99%98%EC%9C%A8_%EC%B5%9C%EC%A2%85.csv"
            try:
                data = pd.read_csv(url)

                # Convert the '일자' column to datetime format and sort the data by date
                data['일자'] = pd.to_datetime(data['일자'])
                data = data.sort_values(by='일자')

                # Plot the data using Plotly Express
                fig = px.line(data, x='일자', y='원/달러', title='원/달러 (2020-2023)')
                fig.update_traces(line=dict(color='#008d62'))
                st.plotly_chart(fig)
                # sub 설명 텍스트
                st.write("출처:지표누리(https://www.index.go.kr/unity/potal/main.do)")

            except Exception as e:
                st.write("데이터를 불러오는 중 문제가 발생했습니다:", str(e))
        elif stat_option == "금 시세":
            # External data loading
            url = "https://raw.githubusercontent.com/Waterrrrrit/2025-01-TheFree/refs/heads/main/iG_2020-2023_filled.csv"
            try:
                data = pd.read_csv(url)

                # Convert the '일자' column to datetime format and sort the data by date
                data['일자'] = pd.to_datetime(data['일자'])
                data = data.sort_values(by='일자')

                # Plot the data using Plotly Express
                fig = px.line(data, x='일자', y='원/g_시가', title='원/g_시가 (2020-2023)')
                fig.update_traces(line=dict(color='#008d62'))
                st.plotly_chart(fig)
                                # sub 설명 텍스트
                st.write("출처:한국거래소(http://data.krx.co.kr/contents/MDC/MAIN/main/index.cmd)")
            except Exception as e:
                st.write("데이터를 불러오는 중 문제가 발생했습니다:", str(e))

        elif stat_option == "국제 유가":
                        # External data loading
            url = "https://raw.githubusercontent.com/Waterrrrrit/2025-01-TheFree/refs/heads/main/%EC%9C%A0%EA%B0%80file2.csv"
            try:
                data = pd.read_csv(url)

                # Convert the '일자' column to datetime format and sort the data by date
                data['일자'] = pd.to_datetime(data['일자'])
                data = data.sort_values(by='일자')

                # Plot the data using Plotly Express
                fig = px.line(data, x='일자', y='달러/배럴', title='달러/배럴 (2020-2023)')
                fig.update_traces(line=dict(color='#008d62'))
                st.plotly_chart(fig)
                # sub 설명 텍스트
                st.write("출처: 한국석유공사(https://www.knoc.co.kr/)")
            except Exception as e:
                st.write("데이터를 불러오는 중 문제가 발생했습니다:", str(e))

        else:
                        # External data loading
            url = "https://raw.githubusercontent.com/Waterrrrrit/2025-01-TheFree/refs/heads/main/%EC%9C%A0%EB%A5%98%EC%84%B8_%EC%B5%9C%EC%A2%85.csv"
            try:
                data = pd.read_csv(url)

                # Convert the '일자' column to datetime format and sort the data by date
                data['일자'] = pd.to_datetime(data['일자'])
                data = data.sort_values(by='일자')

                # Plot the data using Plotly Express
                fig = px.line(data, x='일자', y='원/리터', title='원/리터 (2020-2023)')
                fig.update_traces(line=dict(color='#008d62'))
                st.plotly_chart(fig)
                # sub 설명 텍스트
                st.write("출처:한국석유공사(https://www.knoc.co.kr/)")
            except Exception as e:
                st.write("데이터를 불러오는 중 문제가 발생했습니다:", str(e))

            
else:
    st.write("사이드바에서 비교 모델 또는 지표를 선택해주세요.")


