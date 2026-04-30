import pickle 
from flask import Flask,request,jsonify,render_template

app=Flask(__name__)

model=pickle.load(open("model.pkl","rb"))
vectorizer=pickle.load(open("vectorizer.pkl","rb"))
model_phishing = pickle.load(open("model_phishing.pkl", "rb"))
vectorizer_phishing = pickle.load(open("vectorizer_phishing.pkl", "rb"))

# --- Spam Detection --- #
def predict_spam(text):
    vector = vectorizer.transform([text])
    result = model.predict(vector)[0]

    prediction = ""
    css_class = ""

    if result == 1:
        prediction = "SPAM"
        css_class = "spam"
    else:
        prediction = "HAM"
        css_class = "ham"

    return prediction, css_class

# --- Phishing Detection --- #
def predict_phishing(text):
    vector = vectorizer_phishing.transform([text])
    prob = model_phishing.predict_proba(vector)[0][1]

    percent = round(prob * 100, 2)

    label = ""
    css_class = ""

    if percent < 30:
        label = "Low Risk"
        css_class = "safe"

    elif percent < 70:
        label = "Suspicious"
        css_class = "warning"

    else:
        label = "High Risk"
        css_class = "phishing"

    return percent, label, css_class






# ===== ROUTE ===== #

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    percent = None
    css_class = ""
    mode = "spam"   # default mode

    if request.method == "POST":
        message = request.form["message"]
        mode = request.form["mode"]   

        if mode == "spam":
            prediction, css_class = predict_spam(message)

        elif mode == "phishing":
            percent, prediction, css_class = predict_phishing(message)

    return render_template(
        "index.html",
        prediction=prediction,
        percent=percent,
        css_class=css_class,
        mode=mode
    )


if __name__ == "__main__":
    app.run(debug=True)
