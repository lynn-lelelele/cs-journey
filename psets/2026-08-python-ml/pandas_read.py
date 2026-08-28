import pandas as pd

movies = pd.read_csv("movies.csv")
print(movies)
print(movies["genre"].value_counts())
