from pandasai import SmartDataframe
from pandasai.llm import GoogleGemini
import pandas as pd
import streamlit as st
import seaborn as sns
def pandas_ai(df):
    llm = GoogleGemini(api_key='YOUR_API_KEY')
    sm = SmartDataframe(df,config={'llm':llm})
    # response = sm.chat(prompt+query)
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    if query := st.chat_input("Enter Your Query"):
        st.chat_message("user").markdown(query)
        st.session_state.messages.append({"role": "user", "content": query})
        response = sm.chat(query)
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content":response})
        if 'temp_chart' in str(response):
            st.image(response)
        else:
            st.write(response)
def main():
    st.set_page_config('pandasai_data_analyst')
    st.title('PandasAI Analysis')
    st.header('Do The simpler Analytics task without any coding.....')
    file = st.file_uploader('Upload Your Csv Data', type=['csv'])
    df=None
    if file:
        data = pd.read_csv(file)
        pandas_ai(data)
if __name__ == '__main__':
    main()
