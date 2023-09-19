import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('trained_model.sav','rb'))

def diabetes_prediction(input_data):


    input_data = np.asarray(input_data).reshape(1, -1)

    prediction = loaded_model.predict(input_data)
    print(prediction)
    try:
        if (prediction[0] == 0):
            return 'The person is not Diabetic'

        else:
            return 'The person is Diabetic'
    except ValueError:
        print('Enter Valid Inputs')

def main():

    st.title('Diabetes Prediction App')

    Pregnancies = st.text_input('Number of Pregnancies')

    Glucose = st.text_input('Glucose Level')

    BloodPressure = st.text_input('Blood Pressure')

    SkinThickness = st.text_input('Skin Thickness')

    Insulin = st.text_input('Insulin Level')

    BMI = st.text_input('BMI Value')

    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')

    Age = st.text_input('Age')


    diagnosis = ''

    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

    if diagnosis:
        st.success(diagnosis)
    else:
        st.error('Enter Valid Inputs')

if __name__ == '__main__':
    main()
