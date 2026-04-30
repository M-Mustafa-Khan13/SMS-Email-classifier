import pickle

model = pickle.load(open("model_phishing.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer_phishing.pkl", "rb"))

def get_phishing_score(text, model, vectorizer):
    vector = vectorizer.transform([text])
    prob = model.predict_proba(vector)[0][1]
    return round(prob * 100, 2)


print(get_phishing_score("verify your account immediately", model, vectorizer))