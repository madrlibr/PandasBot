import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import pandas as pd

class processor:
    def __init__(self, user_input, model, integers):
        self.user_input = user_input
        self.model = model
        self.integers = integers

    def process(self):
        tfidf = TfidfVectorizer()
        df = pd.read_csv('notebooks/dataset/sentence.csv')
        X = tfidf.fit_transform(df['text'])
        self.integers = 0
        isdigit = bool(re.search(r'\d', self.user_input))
        if isdigit == True:
            breaking = re.findall(r'\d+', self.user_input)
            integers = "".join(breaking)
            self.integers = int(integers)

        self.user_input = tfidf.transform([self.user_input])
        predict = self.model.predict(self.user_input)[0]
        predict = int(predict)

        return predict, self.integers