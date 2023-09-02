import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='School',
    page_icon='🏫'
)

menu = st.sidebar.selectbox(
    'Menu', ['BMI Calculator', 'Circle Area Calculator', 'GPA Calculator'])

# BMI계산기
if menu == 'BMI Calculator':
    st.subheader('BMI Calculator')

    h = (st.number_input('Enter Your Height (cm)', 1, step=1))/100
    w = st.number_input('Enter Your Weight (kg)', 1, step=1)
    bmi = w/(h*h)

    btn = st.button('Calculate')
    if btn:
        st.write('Your BMI index is ', bmi)

        if bmi < 18.5:
            st.write('저체중')
        elif 18.5 <= bmi <= 22.9:
            st.write('정상')
        elif 23.0 <= bmi <= 24.9:
            st.write('과체중')
        elif 25 <= bmi <= 22.9:
            st.write('경도비만')
        elif 30 <= bmi:
            st.write('중등도비만')

# 원넓이계산기
elif menu == 'Circle Area Calculator':
    st.subheader('Circle Area Calculator')

    r = st.number_input('원의 반지름')
    a = 3.14*r**2

    btn = st.button('Calculate')
    if btn:
        st.write('원의 넓이는 ', a, '입니다.')

# 등급계산기
elif menu == 'GPA Calculator':
    st.subheader('GPA calculator')

    p = st.number_input('점수', 1, 100, step=1)

    if 90 < p <= 100:
        g = 'A'
    elif 80 < p <= 90:
        g = 'B'
    elif 70 < p <= 80:
        g = 'C'
    elif 60 < p <= 70:
        g = 'D'
    elif 50 < p <= 60:
        g = 'E'
    elif p <= 50:
        g = 'F'

    btn = st.button('Calculate')
    if btn:
        st.write('당신의 등급은 ', g, '입니다.')

        df = pd.DataFrame({
            '점수': ['91~100', '81~90', '71~80', '61~70', '51~60', '0~50'],
            '등급': ['A', 'B', 'C', 'D', 'E', 'F']
        })

        st.dataframe(df)
