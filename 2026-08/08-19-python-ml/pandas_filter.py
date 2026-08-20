import pandas as pd

movies = pd.DataFrame({
    "title": ["Inception", "Titanic", "Avatar", "Interstellar"],
    "rating": [8.8, 7.9, 7.9, 8.7],
    "year": [2010, 1997, 2009, 2014]
})

high = movies[movies["rating"] >= 8.0]
print(high)
print(movies.sort_values("rating", ascending=False))
