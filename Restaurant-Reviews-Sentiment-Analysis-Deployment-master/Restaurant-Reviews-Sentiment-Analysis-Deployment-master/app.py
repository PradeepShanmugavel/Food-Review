# Importing essential libraries
from flask import Flask, render_template, request
import pickle

# Load the Multinomial Naive Bayes model and CountVectorizer object from disk
filename = 'restaurant-sentiment-mnb-model.pkl'
classifier = pickle.load(open(filename, 'rb'))
cv = pickle.load(open('cv-transform.pkl', 'rb'))

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)
