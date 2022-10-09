from pymagnitude import Magnitude, MagnitudeUtils
from fastapi import FastAPI
from pydantic import BaseModel
from lib import sent2vec, sents2sim
from typing import TypedDict

magnitude = Magnitude(MagnitudeUtils.download_model("chive-1.2-mc90", remote_path="https://sudachi.s3-ap-northeast-1.amazonaws.com/chive/"))

app = FastAPI()

class Rv(BaseModel):
    words: list[str]

class RvTarget(TypedDict):
    id: int
    sent: list[str]

class RvSents(BaseModel):
    base: list[str]
    targets: list[RvTarget]


@app.get("/")
def read_root():
    return {"Hello": "World!"}

@app.post("/targets")
def post_targets(rv: RvSents):
    sims = []
    base_vec = sent2vec(magnitude, rv.base)
    for target in rv.targets:
        target_vec = sent2vec(magnitude, target["sent"])
        sims.append({
            "id": target["id"],
            "sim": sents2sim(base_vec, target_vec)
        })
    return sims