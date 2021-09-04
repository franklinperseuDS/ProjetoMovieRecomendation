import pandas as pd

import urllib.request
import json

filmes = pd.read_csv("movies.csv")
classess = pd.read_csv("filmes-Final.csv")

print(classess.info())

classe_final = 3
grupo_classificados = classess[classess["class"] == classe_final]

grupo_classificados =  grupo_classificados.sort_values(by=['nota_media'], ascending=False)

grupo_classificados = grupo_classificados[grupo_classificados["nota_media"] > 3]
grupo_classificados = grupo_classificados.sample(n=5)
for i in range(3):
    print(filmes['title'][filmes["movieId"] == grupo_classificados.iloc[i,1]])


