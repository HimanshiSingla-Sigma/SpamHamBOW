from flask import Flask,request,render_template
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

application = Flask(__name__)
app = application

with open("models/spamham.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/bow.pkl", "rb") as f:
    cv = pickle.load(f)

def preprocess(text):
    """
    Clean and preprocess the input text:
    - Keep only letters
    - Lowercase
    - Tokenize
    - Remove stopwords
    - Lemmatize
    """
    # Keep only letters
    text = re.sub('[^a-zA-Z]', ' ', text)
    # Lowercase
    text = text.lower()
    # Tokenize
    words = text.split()
    # Remove stopwords and lemmatize
    words = [lemmatizer.lemmatize(word) for word in words if word not in stopwords.words("english")]
    return ' '.join(words)

@app.route("/")
def home():
    return render_template("index.html") 

@app.route("/predict",methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        message = request.form.get('message')
        cleaned_message = preprocess(message)
        message_bow = cv.transform([cleaned_message]).toarray()
        prediction = model.predict(message_bow)[0]
        result = "Ham" if prediction == 0 else "Spam"
        
        return render_template('home.html', result=result)
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)