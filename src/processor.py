from sklearn.feature_extraction.text import TfidfVectorizer
import re
import pandas as pd

class processor:
    def __init__(self, user_input, model, number):
        self.user_input = user_input
        self.model = model
        self.number = number

    def process(self):
        tfidf = TfidfVectorizer()
        df = pd.read_csv('notebooks/dataset/sentence.csv')
        X = tfidf.fit_transform(df['text'])
        self.number = 0
        isdigit = bool(re.search(r'\d', self.user_input))
        if isdigit == True:
            breaking = re.findall(r'\d+', self.user_input)
            number = "".join(breaking)
            self.number = int(number)

        self.user_input = tfidf.transform([self.user_input])
        predict = self.model.predict(self.user_input)[0]
        predict = int(predict)
        number = int(self.number)
        
        return predict, number