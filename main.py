import gensim

vectors = gensim.models.KeyedVectors.load(\
    "./chive-1.2-mc90_gensim/chive-1.2-mc90.kv")

# "すだち" in vectors # False, v1.1では正規化されているため
# "酢橘" in vectors # True

import time 
s = time.time()
print(vectors["酢橘"])
e = time.time()
print(e-s)
# array([-5.68204783e-02, -1.26615226e-01,  3.53190415e-02, -3.67305875e-01, ...])

# vectors.similarity("酢橘", "徳島")
# 0.3993048

# vectors.most_similar("徳島", topn=5)
# [('愛媛', 0.8229734897613525),
# ('徳島県', 0.786933422088623),
# ('高知', 0.7795713543891907),
# ('岡山', 0.7623447179794312),
# ('徳島市', 0.7415297031402588)]

# vectors.most_similar(positive=["阿波", "高知"], negative=["徳島"], topn=5)
# [('土佐', 0.620033860206604),
# ('阿波踊り', 0.5988592505455017),
# ('よさこい祭り', 0.5783430337905884),
# ('安芸', 0.564490556716919),
# ('高知県', 0.5591559410095215)]