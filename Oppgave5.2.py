# Fra oppgave 5.1:

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
    print(f"{i['name']} - {i['year']} has a rating of {i['rating']}")

def average_rating(movielist):
    rating = 0
    number_of_movies = len(movielist)

    for movie in movielist:
        rating += movie['rating']

    if number_of_movies > 0:
        average = rating / number_of_movies
    else:
        average = 0
    return average
print(f"\nGjennomsnittlig rating for filmene: {round(average_rating(movies),2)}")

def from_year(movielist, year):
    movies_from_year = []
    for movie in movielist:
        if movie['year'] >= year:
            movies_from_year.append(movie)
    return movies_from_year

movies_from_year = from_year(movies, 2010)
print()

for movie in movies_from_year:
    print(f"{movie['name']} - {movie['year']} - {movie['rating']}")