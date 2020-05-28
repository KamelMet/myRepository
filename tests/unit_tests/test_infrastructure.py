import os
import pytest
import pandas as pd

from basicmlapp.infrastructure import load_train_data, save_model, load_model


test_data_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'resources')
test_file_1 = os.path.join(test_data_dir, 'test_data.csv')
test_file_2 = os.path.join(test_data_dir, 'test_data_dont_exist.csv')


@pytest.mark.parametrize("file_path,expected", [(test_file_1, 8), (test_file_2, 0)])
def test_load_train_data(monkeypatch, file_path, expected):
    def mock_path_join(data_dir, file_name):
        return file_path

    monkeypatch.setattr(os.path, "join", mock_path_join)

    train_df = load_train_data()
    assert isinstance(train_df, pd.DataFrame)
    assert len(train_df.index) == expected


def test_save_model():
    # TODO: write test
    pass


def test_load_model():
    # TODO: write test
    pass
