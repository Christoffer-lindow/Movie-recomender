class Movie:
    def __init__(self, movie_id, movie_name, year):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.year = year
        self.ratings = []

    def __repr__(self):
        return {"movie_id": self.movie_id}

    def __str__(self):
        return F"Movie id: {self.movie_id}, Movie name: {self.movie_name}, Year: {self.year}, ratings: {self.ratings}"


class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.ratings = []

    def set_movie_ratings(self, ratings):
        self.movie_ratings = ratings

    def __repr__(self):
        return {"user_id": self.user_id}

    def __str__(self):
        return F"user_id: {self.user_id}, user_name: {self.user_name}, ratings: {self.ratings}"


class Rating:
    def __init__(self, user_id, movie_id, rating):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating

    def __repr__(self):
        return {"user_id": self.user_id, "movie_id": self.movie_id, "rating": self.rating}

    def __str__(self):
        return F"user_id: {self.user_id}, movie_id: {self.movie_id}, rating: {self.rating}"
