import re
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

def dinfo(x): #this function isn't working yet
    x = x.info()
    return x
            
def ddescribe(x):
    x = x.describe()
    return x
        
def dhead(x, n):
    x = x.head(n)
    return x
        
def ddropna(x):
    x = x.dropna()
    return x
        
def dtail(x, n):
    x = x.tail(n)
    return x

class makeice:
    def __init__(self, data):
        self.data = data
        self.length = len(data.columns)
        self.container = {}

    def breakice(self):
        for i in range(0, self.length):
            key = int(i)
            self.container[key] = self.data.iloc[:, i]


def pcolumn(x, n):
    obj = makeice(x)
    obj.breakice()
    try:
        return obj.container[n]
    except:
        pass


class processor:
    def __init__(self, user_input, model, integers):
        self.user_input = user_input
        self.model = model
        self.integers = integers

    def process(self):
        X = joblib.load("model/ftransform")
        tfidf = TfidfVectorizer()
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