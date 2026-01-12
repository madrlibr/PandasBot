import streamlit as st
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

#INIT MODEL
loaded_model = joblib.load('model/panda.joblib')
tfidf = TfidfVectorizer()
model = loaded_model
df = pd.read_csv('notebooks/dataset/sentence.csv')
X = tfidf.fit_transform(df['text'])


st.title("Panda Helper Chatbot 🐼")

uploaded_file = st.sidebar.file_uploader("Upload file CSV", type=["csv"])
existing_dataset = st.pills("Dataset yang tersedia", ["dummy/datas.csv"] )

if uploaded_file or existing_dataset:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File berhasil diunggah!")
    except: 
        df = pd.read_csv("dummy/datas.csv")
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
        
        
        #Function
        def dinfo(x): #this function isn't working yet
            x = x.info()
            return x
            
        def ddescribe(x):
            x = x.describe()
            return x
        
        def dhead(x):
            x = x.head(5)
            return x
        
        def ddropna(x):
            x = x.dropna()
            return x
        
        def dtail(x):
            x = x.tail(5)
            return x

        func = {
            1: df,
            2: ddescribe(df),
            3: dinfo(df),
            4: ddropna(df),
            5: dhead(df),  
            6: dtail(df)
        }
        
        response = {
            1: "Menampilkan seluruh baris",
            2: "Deskripsi dataset",
            3: "Informasi dataset",
            4: "Menghapus baris berisi NULL/NaN",
            5: "Memuat 5 baris pertana",
            6: "Memuat 5 baris terakhir"
        }
        user_input = prompt.lower()
        user_input = tfidf.transform([user_input])
        predict = model.predict(user_input)[0]
        predict = int(predict)
        output_data = func[predict]
        response_text = response[predict]
        

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
