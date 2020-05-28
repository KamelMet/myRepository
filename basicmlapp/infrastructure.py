"""loading data."""

import logging
import os
import pandas as pd
import joblib

from basicmlapp import settings


def load_train_data():
    path = os.path.join(settings.DATA_DIR, settings.DATA_FILE)
    if os.path.exists(path):
        train_df = pd.read_csv(path)
        logging.info("Loading train data successful")
    else:
        train_df = pd.DataFrame()
        logging.info("Train data are empty")
    return train_df


def save_model(model, method):
    dir_path = os.path.join(settings.DATA_DIR, settings.MODEL_DIR)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    path = os.path.join(dir_path, method + '_model.pkl')
    joblib.dump(model, path)
    return "model based on {} successfully saved".format(method)


def load_model(method):
    dir_path = os.path.join(settings.DATA_DIR, settings.MODEL_DIR)
    path = os.path.join(dir_path, method + '_model.pkl')
    model = joblib.load(path)
    return model


if __name__ == '__main__':
    load_train_data()
