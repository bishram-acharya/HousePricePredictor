import base64
import streamlit as st
import pickle
import pandas as pd
import numpy as np
model = pickle.load(
    open('C:/Users/bisra/Desktop/prac2/trained_model.sav', 'rb'))

# creating a function for Prediction


def prices_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data, dtype=object)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = model.predict(input_data_reshaped)
    ans = prediction[0]
    return np.array(ans)


def main():
    prediction = ''
    ans = ''
    st.title("House Price Predictor(Boston)")

    # Parameter value assignment
    crime = st.text_input('Per capita crime rate by town')
    Zn = st.text_input(
        'Proportion of residential land zoned for lots over 25,000 sq.ft.')
    Indus = st.text_input('Proportion of non-retail business acres per town.')
    Chas = st.selectbox(
        'Charles River (1 if tract bounds river; 0 otherwise)', ('0', '1'))
    Nox = st.text_input('Nitric oxides concentration (parts per 10 million)')
    Rm = st.text_input('Average number of rooms per dwelling')
    Age = st.text_input(
        'Proportion of owner-occupied units built prior to 1940')
    Dis = st.text_input('Weighted distances to five Boston employment centres')
    Rad = st.text_input('Index of accessibility to radial highways')
    Tax = st.text_input('full-value property-tax rate per $10,000')
    Ptratio = st.text_input('pupil-teacher ratio by town')
    bk = st.text_input(
        '1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town')
    Lstat = st.text_input('% lower status of the population')

    # Help Sidebar
    st.sidebar.title('Help')
    st.markdown(
        f'''
            <style>
                .sidebar .sidebar-content {{
                    width: 450px;
                }}
            </style>
        ''',
        unsafe_allow_html=True
        # this allows changing sidebar width
    )
    st.sidebar.text('''
    Enter the all the parameters
    related to your house and
    press the \'PREDICT\'
    button to predict your house price''')

    # Predict button
    arr = 0
    if st.button('PREDICT'):
        arr = prices_prediction([crime, Zn, Indus, Chas, Nox, Rm, Age,
                                 Dis, Rad, Tax, Ptratio, bk, Lstat])
    arr = round(arr*1000, 2)
    text = f'The Predicted Price of your House is ${arr}'
    st.success(text)


if __name__ == '__main__':
    main()
