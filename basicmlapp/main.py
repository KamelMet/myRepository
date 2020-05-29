#!/usr/bin/env python3
# coding: utf-8

import logging
from flask import Flask, request, jsonify
import pandas as pd

from basicmlapp import settings
from basicmlapp import infrastructure
from basicmlapp import modelling

app = Flask(__name__)
logging.basicConfig(
    format=settings.LOGGING_FORMAT,
    datefmt=settings.LOGGING_DATE_FORMAT,
    level=settings.LOGGING_LEVEL,
)


@app.route("/mlmethods")
def get_mlmethods():
    """TODO."""
    return jsonify(settings.available_methods)


@app.route("/train", methods=["POST"])
def train():
    df = infrastructure.load_train_data()
    method = request.get_json()["method"]
    logging.info("Starting training based on method : {}".format(method))
    model = modelling.train_model(df, method)
    saving_result = infrastructure.save_model(model, method)
    return jsonify(saving_result)


@app.route("/predict", methods=["POST"])
def predict():
    method = request.get_json()["method"]
    model = infrastructure.load_model(method)
    logging.info("Starting prediction based on method : {}".format(method))
    data = request.get_json()["data"]
    df = pd.DataFrame([data], columns=settings.numeric_features + settings.categorical_features)
    result = model.predict(df).tolist()
    return jsonify(result)


@app.route("/allpredictions")
def get_allprediction():
    """TODO."""
    return jsonify("")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
