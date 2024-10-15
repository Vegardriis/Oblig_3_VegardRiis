
movies = [
    {"name": "Inception", "year": 2010, "rating": 8.7},
    {"name": "Inside Out", "year": 2015, "rating": 8.1},
    {"name": "Con Air", "year": 1997, "rating": 6.9}
]


def add_movie(movielist, name, year, rating = 5.0):
    new_movie = {"name": name, "year": year, "rating": rating}
    movielist.append(new_movie)
    return movielist

add_movie(movies,"Dune", 2021, 8.0)

add_movie(movies,"Joker: Foile à Deux", 2024, )

add_movie(movies,"Dear John", 2010, 6.3)

for i in movies:
    print(i)