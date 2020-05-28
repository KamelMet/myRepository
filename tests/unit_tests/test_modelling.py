from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.utils.validation import check_is_fitted

from basicmlapp import settings
from basicmlapp.modelling import make_pipeline, make_preprocessor
from basicmlapp.modelling import gridsearch, train_model


def test_train_model(sample_df):
    # TODO: mock gridsearch
    fitted_clf = train_model(sample_df)
    for step in fitted_clf.steps:
        assert check_is_fitted(fitted_clf[1]) is None
    assert isinstance(fitted_clf, Pipeline)


def test_make_preprocessor():
    numeric = settings.numeric_features
    cat = settings.categorical_features
    preprocessor = make_preprocessor(numeric, cat)
    assert isinstance(preprocessor, ColumnTransformer)


def test_make_pipeline():
    numeric = settings.numeric_features
    cat = settings.categorical_features
    pipeline = make_pipeline(numeric, cat, "random_forest")

    assert isinstance(pipeline, Pipeline)
    assert len(pipeline.steps) > 0  # no empty pipeline


def test_gridsearch(sample_X, sample_y):
    clf = make_pipeline(settings.numeric_features, settings.categorical_features, "random_forest")
    estimator = gridsearch(sample_X, sample_y, clf, settings.paramgrid, settings.cv)
    assert isinstance(estimator, GridSearchCV)
