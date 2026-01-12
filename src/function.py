import random as rd
import pandas as pd


def randomizer(t):
    while True:
        return rd.randint(0,t)

def getlen(name):
    return len(name) - 1

#the function bellow can't imported yet
def dinfo(df):
    df.info()

def ddescribe(df):
    df.describe()

def dhead(df):
    df.head(5)
