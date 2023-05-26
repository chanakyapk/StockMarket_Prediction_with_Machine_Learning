import pandas as pd
import streamlit as st 
import pickle

st.title('Reliance Industries Future Predictions')

st.sidebar.header('User Input Parameters')

def user_input_features():
    Holding = st.sidebar.selectbox('Minimum how many months can you Holding ?',('1','2','3','4','5','6','7','8','9','10','11','12'),)
    Expectations = st.sidebar.number_input('What Percentage of profit do you expect?')

    data = {'Holding':Holding,
            'Expectations':Expectations,
            }
    features = pd.DataFrame(data,index = [0])
    return features 
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)
load_model=pickle.load(open(r"C:\Users\cpakh\projects\StockMarket_Prediction\Model.sev","rb"))


last=2498.50
prediction = load_model.predict(start = 259, end = 259+int(df['Holding'][0:1]))

percentage=(max(prediction)-last)/last
per=round(percentage*100,2)
st.subheader('Predicted Result')
st.write('Yes, Invester can invest' if per > float(df['Expectations'][0:1]) else 'No, It would be risky to Invest')

st.subheader('Maximum Predicted Price')
st.write(round(max(prediction)))

st.subheader('Maximum Predicted Percentage')
st.write(f'{per}%')