import pandas as pd

import urllib.request
import json

filmes = pd.read_csv("movies.csv")

print(filmes.head())