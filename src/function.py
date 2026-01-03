import random
import pandas as pd

def randomizer(t):
    while True:
        return random.randint(0,t)

def getlen(name):
    return len(name) - 1

def clean_d(df):
    df = df.dropna()
    df = df.drop_duplicates()
    return df

func_list = {
    "r": randomizer,
    "gl": getlen,
    "cl": clean_d
}