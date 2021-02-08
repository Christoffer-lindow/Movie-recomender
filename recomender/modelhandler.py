import csv
from recomender.models import Movie, User, Rating


def add_movie_ratings_to_users(user_list, rating_list):
    for user in user_list:
        for rating in rating_list:
            if (user.user_id == rating.user_id):
                user.ratings.append(
                {"movie_id": rating.movie_id, "rating": rating.rating})

def add_user_ratings_to_movies(movie_list, rating_list):
    for movie in movie_list:
        for rating in rating_list:
            if (movie.movie_id == rating.movie_id):
                movie.ratings.append(
                {"user_id": float(rating.user_id), "rating": float(rating.rating)})

def get_reduced_movie_list(user, movie_list):
    temp_movie_list = movie_list.copy()
    for rating in user.ratings:
        for movie in movie_list:
            if rating["movie_id"] == movie.movie_id:
                temp_movie_list.remove(movie)
    return temp_movie_list

def create_movie_list(dataUrl):
    movie_list = []
    with open(dataUrl) as movie_file:
        csv_reader = csv.reader(movie_file, delimiter=";")
        lines_count = 0
        for row in csv_reader:
            if lines_count != 0:
                movie_list.append(Movie(row[0], row[1], row[2]))
            lines_count += 1
    return movie_list


def create_rating_list(dataUrl):
    rating_list = []
    with open(dataUrl) as rating_file:
        csv_reader = csv.reader(rating_file, delimiter=";")
        lines_count = 0
        for row in csv_reader:
            if lines_count != 0:
                rating_list.append(Rating(row[0], row[1], row[2]))
            lines_count += 1
    return rating_list


def create_user_list(dataUrl):
    user_list = []
    with open(dataUrl) as user_file:
        csv_reader = csv.reader(user_file, delimiter=";")
        lines_count = 0
        for row in csv_reader:
            if lines_count != 0:
                user_list.append(User(row[0], row[1]))
            lines_count += 1
    return user_list
