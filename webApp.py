import string
from flask import Flask, render_template, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__, template_folder='templates',
            static_folder="static")

@app.route('/')
def home():
    return render_template('textapp.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['message']
        lower_case = text.lower()
        cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
        res = sentiment_analyse(cleaned_text)
        return render_template('resulttext.html', prediction=res)

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    if score['neg'] > score['pos']:
        return 1
    elif score['neg'] < score['pos']:
        return 2
    else:
        return 3

if __name__ == '__main__':
    app.run(debug=True)

#ShivamRanjan
