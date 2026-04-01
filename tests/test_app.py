from unittest.mock import MagicMock

import pytest

from cinesense.web.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page(client, mocker):
    """Test the home page."""
    mock_recommender = MagicMock()
    mock_recommender.get_suggestions.return_value = ["Movie 1", "Movie 2"]
    mocker.patch("cinesense.web.app.get_recommender", return_value=mock_recommender)

    rv = client.get("/")
    assert rv.status_code == 200
    assert b"Movie Recommendation System" in rv.data
