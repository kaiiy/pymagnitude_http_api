from pymagnitude import Magnitude, MagnitudeUtils
from fastapi import FastAPI
from pydantic import BaseModel

vectors = Magnitude(MagnitudeUtils.download_model("chive-1.2-mc90", remote_path="https://sudachi.s3-ap-northeast-1.amazonaws.com/chive/"))

app = FastAPI()

class Rv(BaseModel):
    words: list[str]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/")
def post_magnitude(rv: Rv):
    parsed = []
    for word in rv.words:
        parsed.append({
            "word": word,
            "vec": vectors.query(word).tolist()
        })
    return parsed