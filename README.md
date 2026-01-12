# PandaBot
A Python-based application that allows users to interact with CSV datasets using natural language commands in Indonesian. The system processes user input through a rule-based engine to 
execute specific Pandas functions and displays the results via a Streamlit web interface.

## Requirements
    Python 3.x
    Pandas
    Streamlit
    Sklearn


## Footage
<img width="1555" height="1009" alt="Screenshot (1182)" src="https://github.com/user-attachments/assets/2bf87720-ed09-45f9-ab76-e86ed7438b76" />

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/pandas-chatbot.git

```


2. Navigate to the project directory:
```bash
cd panda-chatbot

```


3. Install the required dependencies:
```bash
pip install pandas streamlit

```



## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py

```

2. Upload your CSV file through the sidebar or use the dummy dataset i provided.
3. Type commands in the chat input using Indonesian, such as:
* "tampilkan seluruh data" (show all data)
* "berikan info dataset" (get dataset info)
* "deskripsi data" (get statistical description)


## Versions
This repository contains two versions of the chatbot:
1. **Main Branch (Recommended)**: Powered by a Machine Learning model for better intent recognition.
2. **Rule-Based Branch**: The original version using string-matching logic. You can access it by switching to the `rule-based` branch.


## Note
The project is still under development.

## LICENSE
This project is licensed under the MIT LICENSE.