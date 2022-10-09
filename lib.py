from time import time
import numpy as np
from pymagnitude import Magnitude, MagnitudeUtils
import sklearn.preprocessing as sp
import ot

def sent2vec(magnitude: Magnitude, sent: list[str]):
    return np.vstack([magnitude.query(word) for word in sent])

def sents2sim(sent1: list[str], sent2: list[str]) -> int:
    s_len = len(sent1)
    s2_len = len(sent2)
    ms = np.ones((1, s_len)).flatten() / s_len
    ms2 = np.ones((1, s2_len)).flatten() / s2_len
    
    s_norm = sp.normalize(sent1, copy=False) 
    s2_norm = sp.normalize(sent2, copy=False)

    c = 1 - s_norm @ s2_norm.T

    wrd = ot.emd2(ms, ms2, c)
    return wrd

if __name__ == "__main__":
    magnitude = Magnitude(MagnitudeUtils.download_model("chive-1.2-mc90", remote_path="https://sudachi.s3-ap-northeast-1.amazonaws.com/chive/"))

    s = sent2vec(magnitude, ["好き", "食べ物", "何", "です", "か"])
    s2 = sent2vec(magnitude, ["私", "は", "りんご", "が", "好き", "だ"])

    print(sents2sim(s, s2))

