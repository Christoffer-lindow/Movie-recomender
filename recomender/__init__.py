from recomender.modelhandler import add_user_ratings_to_movies, create_movie_list, create_user_list, create_rating_list, add_movie_ratings_to_users, get_reduced_movie_list
from recomender.statistics import get_similarity_list_pearson, get_similarity_list_euclidean, get_recomended_movie
# Read data from files


class Recomender:
    def __init__(self):
        self.movie_list = create_movie_list("./data/movies.csv")
        self.user_list = create_user_list("./data/users.csv")
        self.rating_list = create_rating_list("./data/ratings.csv")
        add_movie_ratings_to_users(self.user_list, self.rating_list)
        add_user_ratings_to_movies(self.movie_list, self.rating_list)

    def get_recomendation_euclidian(self, user_id, length):
        similarity_list_euclidian = get_similarity_list_euclidean(
            self.user_list[user_id-1], self.user_list, len(self.user_list))
        reduced_movie_list = get_reduced_movie_list(
            similarity_list_euclidian[0]["user"], self.movie_list)
        return get_recomended_movie(similarity_list_euclidian, reduced_movie_list, length)

    def get_recomendation_perason(self, user_id, length):
        similarity_list_pearson = get_similarity_list_pearson(
            self.user_list[user_id-1], self.user_list, len(self.user_list))
        reduced_movie_list = get_reduced_movie_list(
            similarity_list_pearson[0]["user"], self.movie_list)
        return get_recomended_movie(similarity_list_pearson, reduced_movie_list, length)

    def get_similarity_list_person_euclidian(self, user_id, length):
        similarity_list_euclidian = get_similarity_list_euclidean(
            self.user_list[user_id-1], self.user_list, len(self.user_list))
        return similarity_list_euclidian

    def get_similarity_list_person_euclidian(self, user_id, length):
        similarity_list_euclidian = get_similarity_list_euclidean(
            self.user_list[user_id-1], self.user_list, len(self.user_list))
        return similarity_list_euclidian
