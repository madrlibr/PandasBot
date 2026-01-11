import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from src.function import func_list
from src.list import responses_list, keyword_list


st.title("Panda Helper Chatbot 🐼")

uploaded_file = st.sidebar.file_uploader("Upload file CSV", type=["csv"])
existing_dataset = st.pills("Dataset yang tersedia", ["dataset/datas.csv"] )
existing_dataet = existing_dataset

if uploaded_file or existing_dataset:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File berhasil diunggah!")
    except: 
        df = pd.read_csv("dataset/datas.csv")
        st.success("File berhasil diunggah!")


    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if "data" in message:
                st.write(message["data"])

    
    if prompt := st.chat_input("Apa yang bisa saya bantu?"):
        
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        
        response_text = ""
        output_data = None

        user_input = prompt.lower()
        user_input = user_input.split()

        g_len = func_list["gl"](responses_list["g"])
        c_len = func_list["gl"](responses_list["c"])

        if any(i in user_input for i in keyword_list["i"]):
            import io
            buffer = io.StringIO()
            df.info(buf=buffer)
            response_text = responses_list["i"][0]
            output_data = buffer.getvalue()

            
        elif any(i in user_input for i in keyword_list["a"]):
            response_text = {responses_list["a"][0]}
            output_data = df

        elif any(i in user_input for i in keyword_list["g"]):
            response_text = {responses_list["g"][func_list["r"](g_len)]}

        elif any(i in user_input for i in keyword_list["c"]):
            response_text = {responses_list["c"][func_list["r"](c_len)]}

        elif any(i in user_input for i in keyword_list["h"]):
            response_text = {responses_list["h"][0]}
            output_data = df.head()

        elif any(i in user_input for i in keyword_list["t"]):
            response_text = {responses_list["t"][0]}
            output_data = df.tail()

        elif any(i in user_input for i in keyword_list["d"]):
            response_text = responses_list["d"][0]
            df = df.dropna()
            output_data = df

        elif any(i in user_input for i in keyword_list["ds"]):
            response_text = responses_list["ds"][0]
            output_data = df.describe()

        else:
            response_text = "Pesan tidak dikenali, silahkan coba lagi!."

        with st.chat_message("assistant"):
            response_text = ("".join(response_text))
            st.write(response_text)
            if output_data is not None:
                try:
                    st.dataframe(output_data)
                except:
                    st.write(output_data)

        st.session_state.messages.append({
            "role": "assistant", 
            "content": response_text, 
            "data": output_data
        })
else:
    st.info("Silakan unggah file CSV di sidebar atau pilih dataset yang disediakan untuk memulai.")