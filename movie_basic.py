movies = [] #create a list to store all the movies
    

def menu():
    val = input("Enter 'a' if you want to add a movie, 'f' if you want to find a movie, 'l' if you want to list all movies, 'q' if you want to close the file: ")
    while val != 'q':
        if val == 'a':
            add_movie()
        elif val == 'f':
            find_movie()
        elif val == 'l':
            list_movie(movies)
        elif val == 'q':
            print("Stopped programming...")

        val = input(" \n Enter 'a' if you want to add a movie, 'f' if you want to find a movie, 'l' if you want to list all movies, 'q' if you want to close the file: ")


def add_movie():
    movies.append({
        'name':input('Enter the name of the movie : '),
        'director':input("Enter movie director's name: "),
        'year':input('Enter the release year of the movie: ')
    })


def list_movie(movie_list):
    for movie in movie_list:
        show_movie_details(movie)
        

def show_movie_details(movie):
    print(f"Name:{movie['name']}")
    print(f"Director:{movie['director']}")
    print(f"Year:{movie['year']}")
    print(".............................")


def find_movie():
    find_by= input("what property of the movie, are you exactly looking for ? ")
    looking_for= input('what are you searching for ? ')
    
    found_movies= find_by_attribute(movies,looking_for,lambda x:x[find_by])

    list_movie(found_movies)


def find_by_attribute(items, expected,finder):
    found =[]
    for movie in movies:
        if finder(movie) == expected:
            found.append(movie)
    return found

            
menu()
