from flask import request, render_template
from flask import Blueprint

import numpy as np
import pickle

bp = Blueprint("site", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/bandas")
def bandas():
    return render_template("bandas.html")

@bp.route("/welcome", methods=["POST"])
def welcome():
    with open('modelo.pkl', 'rb') as file:
        modelo = pickle.load(file)

    with open('vocabulary.pkl', 'rb') as file:
        vocabulary = pickle.load(file)

    def count_words(lyrics, vocabulary):
        frequency = [0] * len(vocabulary)

        for word in lyrics:
            if word in vocabulary:
                position = vocabulary[word]
                frequency[position] += 1
        return frequency

    lyrics = request.values['letra'].lower().split()
    frequency = count_words(lyrics, vocabulary)

    x = np.array(frequency).reshape(1, -1)
    
    if modelo.predict(x) == 2 and request.values['letra']:
        result = "The Rolling Stones"
    elif modelo.predict(x) == 1 and request.values['letra']:
        result = "The Beatles"
    else:
        result = "É necessário digitar a letra da música!"

    return render_template("index.html", letra=request.values['letra'], resultado=result)

@bp.route("/admin")
def admin():
    return render_template("admin.html")