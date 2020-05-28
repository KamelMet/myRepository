import os
import pytest
import pandas as pd


@pytest.fixture()
def sample_df():
    df = pd.DataFrame([[5.1, 3.5, 1.4, 0.2, 'setosa'],
                       [4.9, 3, 1.4, 0.2, 'setosa'],
                       [4.7, 3.2, 1.3, 0.2, 'setosa'],
                       [4.6, 3.1, 1.5, 0.2, 'setosa'],
                       [5, 3.6, 1.4, 0.2, 'setosa']],
                      columns=['sepal_length', 'sepal_width',
                               'petal_length', 'petal_width', 'species']
                      )
    return df


@pytest.fixture()
def sample_X(sample_df):
    return sample_df.drop('species', axis=1)


@pytest.fixture()
def sample_y(sample_df):
    y = sample_df['species']
    return y


test_data_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'ressources')
