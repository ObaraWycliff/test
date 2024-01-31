
import streamlit as st
import _datetime

# Set page configuration
st.set_page_config(
    page_title="Your Streamlit App",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",  # or "centered" for a centered layout
    initial_sidebar_state="auto",  # "auto", "expanded", "collapsed"
)
#---------------------------------------------------------------------------------------------------------------------------
custom_styles = """
    /* Custom style for changing background color */
    .custom-background {
        background-color: #ff66b2;  /* Pink color */
        padding: 10px;
        border-radius: 10px;
    }
"""
st.markdown(f'<style>{custom_styles}</style>', unsafe_allow_html=True)

import streamlit as st
st.header("YESTERDAYS TECH SOLUTION")
st.subheader("OUR MISION :\n", 
         "Empoering youth-An escape from drugs.")
st.image("/Users/mac/Desktop/Stramlit/App 1/istockphoto-1465723262-170667a.webp", caption="Image caption", use_column_width=True)

st.subheader(" ***** RATED *****")
rate = st.slider("rate:",min_value=0.0,max_value=5.0, step=0.1, value=2.5 )
st.write(f"You have given us a {rate} rating .THANK YOU")

st.subheader("OUR GOAL")
if st.button ("GOALS"):
    st.write("Our GOAL is to ensuer data literacy in Kenya and Africa as a whole")

st.subheader("OUR OBJECTIVE")
if st.button ("OBJECTIVES"):
    st.write("Youth domination in data science by 2030")
    
st.subheader("ARE YOU INTERESTED IN OUR CLASSES")

Yes = st.checkbox("Yes")
if Yes:
    st.write("You are in the right platfrom")

No= st.checkbox("No")
if No:
    st.write("It is okay.You can check the rest of the page ")

check_box_value = st.checkbox("Show contact")
if check_box_value:
    st.write(" zxt.auto.login")

st.subheader("PERSONAL DETAILS")
st.text_input("Kindly eneter your name:")

st.subheader("MORE")
st.text_area("Tell us about yourself: consider the following topics;education, interest and experience")

st.subheader("CONTACT DETAILS")
st.number_input("Enter your telephone/phone number;",step=1)

st.subheader("TIME AND DATE")
time = st.time_input("At what time do  you intend to join us?",_datetime.time(12,  00))
st.date_input("On Which date to you intend to join us?")

st.subheader("AREA OF INTEREST")
options = ["Data science", "Cloud computing ", "Data analytics", "Machine learning"]
choice= st.selectbox("Chose your preference:",options)

st.subheader("MODE OF LEARNING")
options1 = ["Digital", "Physical ", "Blended", "Curriculum based"]
st.multiselect("Select your prefered modes",options1)

st.subheader("CLASS TIME")
options2 = ["Morning", "Afternoon ", "Evening"]
st.radio("Select apropriate",options2)

st.subheader("SUPPORTING DOCUMENTS")
file = st.file_uploader("Kindly upload your documents")

st.title("TRIAL SECTION")

st.file_uploader("Insert file",type=["csv","xlsx"])








    
    
