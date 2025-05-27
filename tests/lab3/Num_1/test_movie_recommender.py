import pytest
from unittest.mock import mock_open, patch
from src.lab3.Num_1.movie_recommender import MovieRecommender
from collections import defaultdict

@pytest.fixture
def mock_movies_csv():
    return """1,The Shawshank Redemption
2,The Godfather
3,The Dark Knight
4,Pulp Fiction
5,Forrest Gump"""

@pytest.fixture
def mock_history_csv():
    return """1,2,3
1,3,5
2,3,4
1,2,3,4,5
2,4"""

@pytest.fixture
def recommender(mock_movies_csv, mock_history_csv):
    with patch("builtins.open", mock_open()) as mock_file:
        mock_file.side_effect = [
            mock_open(read_data=mock_movies_csv).return_value,
            mock_open(read_data=mock_history_csv).return_value
        ]
        rec = MovieRecommender()
        rec.load_data()
    return rec

def test_load_data(recommender):
    assert len(recommender.movie_titles) == 5
    assert recommender.movie_titles[1] == "The Shawshank Redemption"
    assert len(recommender.user_histories) == 5
    assert recommender.user_histories[0] == [1, 2, 3]

def test_recommend(recommender):
    assert recommender.recommend([1, 2]) in ["The Dark Knight", "Pulp Fiction", "Forrest Gump"]
    assert recommender.recommend([3, 5]) == "The Shawshank Redemption"
    
    assert recommender.recommend([99]) == "Нет рекомендаций"
    
    assert recommender.recommend([]) == "Нет рекомендаций"
