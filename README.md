
---

# 📧 Spam–Ham Message Classifier using Bag of Words (BoW)

## 📌 Project Overview

This project is a **Spam–Ham Message Classification system** built using **Natural Language Processing (NLP)** techniques.
It classifies a given text message as **Spam** or **Ham (Not Spam)** using the **Bag of Words (BoW)** approach and a **Machine Learning classifier**.

The goal of this project is to demonstrate how traditional NLP techniques like BoW can be effectively used for text classification problems.

---

## 🚀 Features

* Text preprocessing (cleaning, tokenization, stopword removal)
* Feature extraction using **Bag of Words**
* Machine learning model training and evaluation
* Predicts whether a message is **Spam** or **Ham**
* Simple and easy-to-understand implementation
* Web interface 

---

## 🧠 Concepts Used

* Natural Language Processing (NLP)
* Bag of Words (BoW)
* Text Vectorization
* Supervised Machine Learning
* Binary Classification

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries:**

  * `numpy`
  * `pandas`
  * `nltk`
  * `scikit-learn`
  * `re`
  * `flask`

---


## 🧹 Text Preprocessing Steps

1. Remove special characters and numbers
2. Convert text to lowercase
3. Tokenize the text
4. Remove stopwords
5. Apply lemmatization 

---

## 📊 Feature Extraction – Bag of Words

* Converts text into numerical vectors
* Counts the frequency of words in the corpus
* Ignores grammar and word order
* Creates a vocabulary of most frequent words

Example:

```
Message: "Free money now"
BoW Vector: [1, 1, 1, 0, 0, ...]
```

---

## 🤖 Model Training

* The processed text data is split into **training** and **testing** sets
* A machine learning algorithm (e.g., **Naive Bayes / Logistic Regression**) is trained
* Model performance is evaluated using accuracy and confusion matrix

---

## 📈 Model Evaluation

* **Accuracy Score**
* **Confusion Matrix**
* **Precision & Recall** (optional)

---

## 🧪 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/spam-ham-classifier.git
cd spam-ham-classifier
```

### Run the Application

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 📝 Example Output

| Input Message                | Prediction |
| ---------------------------- | ---------- |
| "Win a free iPhone now!"     | Spam       |
| "Hey, are we meeting today?" | Ham        |

---

## ⚠️ Limitations

* Bag of Words does not capture semantic meaning
* Ignores word order and context
* Performance may drop for unseen vocabulary

---

## 🔮 Future Improvements

* Use **TF-IDF** instead of BoW
* Implement **Word2Vec or GloVe**
* Upgrade to **Deep Learning / BERT**
* Improve UI and add confidence score

---

## 📚 Learning Outcome

* Understanding text preprocessing in NLP
* Hands-on experience with BoW
* Practical application of ML classification
* End-to-end ML project workflow

---

## 👩‍💻 Author

**Himanshi Singla**
📌 AI and ML Engineer and Researcher


