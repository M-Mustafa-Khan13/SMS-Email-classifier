# 🚀 SMS & Email Intelligence Classifier

### 🔍 AI-Powered Spam & Phishing Detection System

An end-to-end **machine learning web application** that classifies messages as **Spam**, **Ham**, or **Phishing** using Natural Language Processing (NLP) and multiple classification models.

---

## 🌐 Live Demo

👉 https://sms-email-classifier-2nmy.onrender.com

> ⚡ Real-time predictions powered by deployed ML models.

---

## 🧠 Core Features

* 📩 **Spam vs Ham Classification**
* 🛡️ **Phishing Email Detection**
* ⚡ **Real-Time Predictions via Web Interface**
* 🎯 **Optimized ML Pipeline for Text Data**

---

## 🤖 Machine Learning Pipeline

### 🔹 Data Processing

* Text cleaning and normalization
* Stopword removal using **NLTK**
* Basic feature engineering (word count, character count)

---

### 🔹 Feature Extraction

* **TF-IDF Vectorization**
  Converts text into numerical features while preserving importance of words.

---

### 🔹 Models Used

* 🧮 **Multinomial Naive Bayes (Primary Model)**
  Chosen for fast and efficient performance on text data.

* 📈 **Logistic Regression**
  Used as a strong baseline model with good generalization and interpretability.

* 🧠 **Support Vector Machine (SVM)** *(Experimented)*
  Evaluated for handling high-dimensional sparse data.

* 🤝 **Voting Classifier (Ensemble Model)**
  Combined predictions from **Naive Bayes, Logistic Regression, and SVM** to improve robustness and reduce model bias.

* 🌲 **Tree-Based Models (Explored)**
  Tested but less effective for sparse text representations.

---

### 🔹 Model Selection Strategy

After experimentation:

* **Naive Bayes** was selected for deployment due to:

  * Fast inference speed ⚡
  * Strong performance on TF-IDF features
  * Simplicity and scalability

* **Logistic Regression** provided competitive results and served as a reliable baseline.

* **Voting Classifier** improved stability but added complexity with only marginal gains.

---

## 📊 System Architecture

```text
User Input → Preprocessing → TF-IDF Vectorizer → ML Model → Prediction Output
```

---

## ⚠️ Limitations & Real-World Considerations

* 📊 **Imbalanced Dataset**
  The dataset used for training is imbalanced, which may lead to:

  * Bias toward the majority class
  * Misclassification of minority-class examples (e.g., phishing or certain spam types)

* 🎯 **False Positives / False Negatives**
  The model may:

  * Flag legitimate messages as spam
  * Miss subtle spam/phishing attempts

* 🧠 **Limited Context Understanding**
  Traditional ML models rely on word frequency and may struggle with:

  * Contextual meaning
  * Semantic interpretation

---

## 🔄 Future Improvements

* ⚖️ Handle imbalance using SMOTE / class weighting
* 🤖 Upgrade to Deep Learning models (LSTM / Transformers)
* 📈 Improve feature engineering
* 🌐 Build REST API for integration
* 🎨 Enhance frontend UI/UX

---

## 💻 Tech Stack

* **Backend:** Flask
* **Machine Learning:** Scikit-learn
* **NLP:** NLTK
* **Frontend:** HTML, CSS
* **Deployment:** Render

---

## 📂 Project Structure

```
├── app.py
├── model.pkl
├── vectorizer.pkl
├── model_phishing.pkl
├── vectorizer_phishing.pkl
├── templates/
├── static/
├── requirements.txt
├── Procfile
```

---

## ⚙️ Run Locally

```bash
pip install -r requirements.txt
python app.py
```

---

## 🚀 Deployment

Deployed on **Render** with:

* Dynamic port binding
* Production-ready environment
* Continuous deployment via GitHub

---

## 👨‍💻 Author

**Muhammad Mustafa Khan**
Computer Science Student | ML & Backend Enthusiast

---

## ⭐ Final Note

This project demonstrates a complete pipeline:

> **Data → Model → Web App → Deployment**

Bridging machine learning concepts with real-world application delivery.
