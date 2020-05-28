import logging
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import GridSearchCV

from basicmlapp import settings


def train_model(df, method):
    X = df.drop(settings.target_feature, axis=1)
    y = df[settings.target_feature].values.ravel()
    clf = make_pipeline(settings.numeric_features, settings.categorical_features, method)
    fitted_clf = gridsearch(X, y, clf, settings.paramgrid, settings.cv)
    logging.info(f"Score: {fitted_clf.best_score_}")
    logging.info(f"Hyperparameters: {fitted_clf.best_params_}")

    return fitted_clf.best_estimator_


def make_preprocessor(numeric_features, categorical_features):
    numeric_transformer = Pipeline(
        steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
    )
    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )
    return preprocessor


def make_pipeline(numeric_features, categorical_features, method):
    if method == "random_forest":
        classifier = RandomForestClassifier()
    elif method == "decision_tree":
        classifier = DecisionTreeClassifier()
    else:
        logging.error(
            "Specified method not yet available: {}. Available methods are :".format(
                method, settings.available_methods
            )
        )
    clf = Pipeline(
        steps=[
            ("preprocessor", make_preprocessor(numeric_features, categorical_features)),
            ("classifier", classifier),
        ]
    )
    return clf


def gridsearch(X, y, clf, param_grid, cv):
    logging.info(f"Launching gridsearch with params= {param_grid}")
    search = GridSearchCV(clf, param_grid, cv=cv)
    search.fit(X, y)
    return search
