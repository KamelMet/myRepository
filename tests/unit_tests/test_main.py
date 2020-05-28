import json
from basicmlapp import main


def test_get_mlmethods():
    main.app.testing = True
    with main.app.test_client() as c:
        response = c.get('/mlmethods')
        assert response.status_code == 200
        assert isinstance(json.loads(response.get_data()), list)


def test_train():
    # TODO: write test
    pass


def test_predict():
    # TODO: write test
    pass


def test_get_allprediction():
    # TODO: write test
    pass
