"""
Contains all configurations for the projectself.
Should NOT contain any secrets.
"""
import os
import logging

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
DATA_DIR = os.path.join(REPO_DIR, 'data')
DATA_FILE = 'raw/data_raw_iris.csv'
MODEL_DIR = 'models/'

available_methods = ['random_forest', 'decision_tree']

target_feature = ['species']
numeric_features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
categorical_features = []
paramgrid = {'preprocessor__num__imputer__strategy': ['mean', 'median'],
             'classifier__max_depth': [10, 20]}
cv = 3

# Logging
LOGGING_FORMAT = '[%(asctime)s][%(levelname)s][%(module)s] %(message)s'
LOGGING_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
LOGGING_LEVEL = logging.DEBUG
