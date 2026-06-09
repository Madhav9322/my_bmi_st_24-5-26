import streamlit as st
import google.genai as genai

google_api_key = st.secrets["google"]["api_key"]
c=genai.Client(api_key=google_api_key)

height =st.selectbox("Enter your height in meter : ", options = [i/100 for i in range(100,250,1)])
weight =st.selectbox("Enter your weight in kg : ", options= [i/10 for i in range(10,5000,1)])
gender =st.selectbox("What's your gender : ", options = ["male","female"])
bmi = weight/(height**2)
st.write (f"Your BMI is : {bmi:.2f}")

promt = f"Let's talk about the BMI of a person {gender}, whose weight and height is {weight} kg and {height} meter"
response = c.models.generate_content (model="gemini-3.5-flash", contents=promt)
st.write(response.text)