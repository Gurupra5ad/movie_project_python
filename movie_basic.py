movies = [] #create a list to store all the movies
    

def menu():
    val = input("Enter 'a' if you want to add a movie, 'f' if you want to find a movie, 'l' if you want to list all movies, 'q' if you want to close the file: ")
    while val != 'q':
        if val == 'a':
            add_movie()
        elif val == 'f':
            find_movie()
        elif val == 'l':
            list_movie()
        elif val == 'q':
            print("Stopped programming...")

        val = input("Enter 'a' if you want to add a movie, 'f' if you want to find a movie, 'l' if you want to list all movies, 'q' if you want to close the file: ")


def add_movie():
    name = input('Enter the name of the movie : ')
    director = input("Enter movie director's name: ")
    year = int(input('Enter the release year of the movie: '))

    movies.append({
        'name':name,
        'director':director,
        'year':year
    })


def list_movie():
    for movie in movies:
        print(f"Name:{movie['name']}")
        print(f"Director:{movie['director']}")
        print(f"Year:{movie['year']}")
        print(".............................")




def find_movie():
    find_name= input('Enter the movie name you want to find: ')
    for movie in movies:
        if(find_name==movie['name']):
            print(f"Name:{movie['name']}")
            print(f"Director:{movie['director']}")
            print(f"Year:{movie['year']}")
            
            

menu()
