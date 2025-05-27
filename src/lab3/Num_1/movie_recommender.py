import csv
from collections import Counter, defaultdict
from typing import List, Dict, Set


class MovieRecommender:
    MOVIES_PATH = "movies.csv"
    HISTORY_PATH = "history.csv"

    def __init__(self):
        self.movie_titles: Dict[int, str] = {}
        self.user_histories: List[List[int]] = []

    def load_data(self):
        with open(self.MOVIES_PATH, encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                self.movie_titles[int(row[0])] = row[1]

        with open(self.HISTORY_PATH, encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                self.user_histories.append([int(x) for x in row])
    def recommend(self, current_user_movies: List[int]) -> str:
        if not current_user_movies:
            return "Нет рекомендаций"
        
        current_set = set(current_user_movies)
        weighted_candidates = defaultdict(float)

        for history in self.user_histories:
            history_set = set(history)
            intersection = current_set & history_set
            
            # Изменили условие для избежания деления на ноль
            if len(intersection) > 0:  # Теперь учитываем любые пересечения
                weight = len(intersection) / len(current_set)
                for movie in history_set - current_set:
                    weighted_candidates[movie] += weight

        if not weighted_candidates:
            return "Нет рекомендаций"

        recommended_movie_id = max(weighted_candidates.items(), key=lambda x: x[1])[0]
        return self.movie_titles.get(recommended_movie_id, "Фильм не найден")

    def input_and_recommend(self):
        user_input = input("Введите ID просмотренных фильмов через запятую: ")
        current_movies = [int(x) for x in user_input.strip().split(",") if x.isdigit()]
        print(self.recommend(current_movies))


if __name__ == "__main__":
    recommender = MovieRecommender()
    recommender.load_data()
    recommender.input_and_recommend()
