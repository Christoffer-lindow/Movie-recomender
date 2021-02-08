import math


def get_similarity_list_euclidean(user, user_list, length):
    similarity_list = []
    for user_in_list in user_list:
        if user_in_list != user:
            similarity = euclidean(user, user_in_list)
            if not similarity <= 0:
                similarity_list.append(
                    {"user": user, "user_compared": user_in_list, "similarity": similarity})

    return sorted(similarity_list, key=lambda i: (i["similarity"]), reverse=True)[:length]



def get_similarity_list_pearson(user, user_list, length):
    similarity_list = []
    for user_in_list in user_list:
        if user_in_list != user:
            similarity = pearson(user, user_in_list)
            if not similarity <= 0:
                similarity_list.append(
                    {"user": user, "user_compared": user_in_list, "similarity": similarity})

    return sorted(similarity_list, key=lambda i: (i["similarity"]), reverse=True)[:length]


def get_recomended_movie(similarity_list, movie_list, length):
    recomended_movie_list = []
    for movie_from_list in movie_list:
        recomended_movie_list.append({"movie_name": movie_from_list.movie_name,
                                      "movie_id": movie_from_list.movie_id, "w_rating": 0, "ratings": 0, "w_avg": 0})
    for item in similarity_list:
        for rating in item["user_compared"].ratings:
            for movie in recomended_movie_list:
                if movie["movie_id"] == rating["movie_id"]:
                    movie["w_rating"] += item["similarity"] * \
                        float(rating["rating"])
                    movie["ratings"] += 1 * item["similarity"]
                    movie["w_avg"] = movie["w_rating"] / movie["ratings"]

    return sorted(recomended_movie_list, key=lambda i: (i["w_avg"]), reverse=True)[:length]


def euclidean(user_a, user_b):
    sim = 0
    n = 0

    for rating_a in user_a.ratings:
        for rating_b in user_b.ratings:
            if rating_a.get("movie_id") == rating_b.get("movie_id"):
                sim += pow((float(rating_a.get("rating")) -
                            float(rating_b.get("rating"))), 2)
                n += 1

    if n == 0:
        return 0

    inverted = 1 / (1 + sim)
    return inverted


def pearson(user_a, user_b):
    sum_a = 0
    sum_b = 0
    sum_a_sq = 0
    sum_b_sq = 0
    p_sum = 0
    n = 0

    for rating_a in user_a.ratings:
        for rating_b in user_b.ratings:
            if rating_a.get("movie_id") == rating_b.get("movie_id"):
                sum_a += float(rating_a.get("rating"))
                sum_b += float(rating_b.get("rating"))
                sum_a_sq += (pow(float(rating_a.get("rating")), 2))
                sum_b_sq += (pow(float(rating_b.get("rating")), 2))
                p_sum += float(rating_a.get("rating")) * \
                    float(rating_b.get("rating"))
                n += 1

    if n == 0:
        return 0

    num = p_sum - (sum_a * sum_b / n)
    den = math.sqrt((sum_a_sq - pow(sum_a, 2) / n)
                    * (sum_b_sq - pow(sum_b, 2) / n))
    return num/den
