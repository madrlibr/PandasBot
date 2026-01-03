from function import func_list
from list import responses_list, keyword_list
import pandas as pd

print("'exit' to close")
input_dataset = str(input("Masukan path dataset: "))
df = pd.read_csv(input_dataset)
df = pd.DataFrame(df)

while True:
    message = str(input("You: ")).lower()
    message_split = message.split()
    g_len = func_list["gl"](responses_list["g"])
    c_len = func_list["gl"](responses_list["c"])
    if message == "exit":
        print("Exit the program!")
        break

    elif any(i in message_split for i in keyword_list["g"]):
        print(f"Bot: {responses_list["g"][func_list["r"](g_len)]}")

    elif any(i in message_split for i in keyword_list["c"]):
        print(f"Bot: {responses_list["c"][func_list["r"](c_len)]}")

    elif any(i in message_split for i in keyword_list["h"]):
        print(f"Bot: {responses_list["h"][0]}")
        print(df.head())

    elif any(i in message_split for i in keyword_list["t"]):
        print(f"Bot: {responses_list["t"][0]}")
        print(df.tail())

    elif any(i in message_split for i in keyword_list["d"]):
        print(f"Bot: {responses_list["d"][0]}")
        df = df.dropna()
        print(df.to_string())

    elif any(i in message_split for i in keyword_list["a"]):
        print(df.to_string())
        print(f"Bot: {responses_list["a"][0]}")

    elif any(i in message_split for i in keyword_list["i"]):
        print(f"Bot: {responses_list["i"][0]}")
        print(df.info())

    elif any(i in message_split for i in keyword_list["ds"]):
        print(f"Bot: {responses_list["ds"][0]}")
        print(df.describe())

    elif any(i in message_split for i in keyword_list["cl"]):
        print(f"\nBot: {responses_list["cl"][0]} \n")
        df = df.dropna()
        df = df.drop_duplicates()
        print(df.to_string())

"""
This project is under development
and code is kind of messy i think, so i try to working on it
Happy new year 2026 btw😊
"""
