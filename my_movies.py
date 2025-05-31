favorite_movies = []

def add_movie(movie):
    favorite_movies.append(movie)
    print(f"'{movie}' was added to the list.")

def remove_movie(movie):
    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"'{movie}' was removed from the list.")
    else:
        print(f"'{movie}' not found.")

def display_movies():
    print(f"Favorite Movies:")
    for movie in favorite_movies:
        print(f"- {movie}")

def count_movies():
    print(f"Number of movies in collection: {len(favorite_movies)}")

def find_movie(movie):
    if movie in favorite_movies:
        print(f"'{movie}' found in list.")
    else:
        print(f"'{movie}' not found in list.")

def clear_movies():
    favorite_movies.clear()
    print(f"All movies removed from list.")

add_movie("Twilight")
add_movie("Twilight New Moon")
add_movie("Twilight Eclipse")
add_movie("Twilight Breaking Dawn Pt. 1")
add_movie("Twilight Breaking Dawn Pt. 2")
add_movie("Hunger Games")

display_movies()

remove_movie("Hunger Games")

display_movies()

count_movies()

find_movie("Twilight")

clear_movies()