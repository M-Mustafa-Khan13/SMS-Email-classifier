
import pickle
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()

cv2=pickle.load(open("vectorizer.pkl","rb"))
model=pickle.load(open("model.pkl","rb"))

def transform_text(text):
    text=text.lower()
    text=nltk.word_tokenize(text)

    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)

    text=y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text=y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


def predict_message(msg):
    transformed=transform_text(msg)
    vector = cv2.transform([transformed])
    result = model.predict(vector)
    if result[0]==1:
        status="SPAM"
    else:
        status="HAM"
    return status