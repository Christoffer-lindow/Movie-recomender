from fastapi import FastAPI
from recomender import Recomender
recomender = Recomender()

app = FastAPI()

@app.get("/pearson/{user_id}")
def get_recomendation_pearson(user_id: int):
    return recomender.get_recomendation_perason(user_id)

@app.get("/euclidian/{user_id}")
def get_recomendation_euclidian(user_id: int):
    return recomender.get_recomendation_perason(user_id)
