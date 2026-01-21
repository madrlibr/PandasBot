import streamlit as st
import pandas as pd
import joblib
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.function import *
from classes import processor

#LOAD MODEL
model = joblib.load('model/panda.joblib')

st.title("Panda Chatbot")

uploaded_file = st.sidebar.file_uploader("Upload file CSV", type=["csv"])
existing_dataset = st.pills("Dataset yang tersedia", ["dummy/StudentPerformance.csv"] )

if uploaded_file or existing_dataset:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File berhasil diunggah!")
    except: 
        df = pd.read_csv("dummy/StudentPerformance.csv")
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
        pro = processor(user_input=user_input, model=model, integers=0)
        predict, integers = pro.process()
        predict = int(predict)
        integers = int(integers)


        func = {
            1: df,
            2: fdescribe(df),
            3: finfo(df),
            4: fdropna(df),
            5: fhead(df, integers),  
            6: ftail(df, integers),
            7: select_column(df, integers),
            8: meancolumn(df, integers),
            9: mediancolumn(df, integers),
            10: sumcolumn(df, integers)
        }
        response = {
            1: "Menampilkan seluruh baris",
            2: "Menampilkan deskripsi dataset",
            3: "Fitur ini belum berfungsi😁!",
            4: "Menghapus baris berisi NULL/NaN",
            5: f"Menampilkan {integers} baris awal",
            6: f"Menampilkan {integers} baris terakhir",
            7: f"Menampilkan kolom dengan index {integers}",
            8: f"Nilai rata-rata/mean dari kolom index ke-{integers} adalah: ",
            9: f"Nilai tengah/median kolom index ke-{integers} adalah: ",
            10: f"Total-nilai/sum dari kolom index ke-{integers} adalah: "
        }


        output_data = func[predict]
        response_text = response[predict]
        
        try:
            with st.chat_message("assistant"):
                response_text = ("".join(response_text))
                st.write(response_text)
                if output_data is not None:
                    try:
                        st.dataframe(output_data)
                    except:
                        st.write(output_data)
        except:
            st.write("Terjadi kesalahan!")

        st.session_state.messages.append({
            "role": "assistant", 
            "content": response_text, 
            "data": output_data
        })
else:
    st.info("Silakan unggah file CSV di sidebar atau pilih dataset yang disediakan untuk memulai.")
