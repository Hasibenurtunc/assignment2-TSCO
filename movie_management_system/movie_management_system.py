class Movie:


    def __init__(self, name, director, year, type):
        self.name = name
        self.director = director
        self.year = year
        self.type = type


    def __str__(self):
        return f"Movie Name: {self.name}, Movie Director: {self.director}, Year of Movie: {self.year}, Type of Movie: {self.type}"


class MovieDirector:
    def __init__(self):
        self.movies = []


    def add_movie(self,name, director, year, type):
        for i in self.movies:
            if i.name == name:
                print(f"{name} movie has been entered before.")
                return

        new_movie =Movie(name, director, year, type)
        self.movies.append(new_movie)
        print(f"'{new_movie}' movie added to the list.")


    def del_movie(self,name):
        for i in self.movies:
            if i.name == name:
                self.movies.remove(i)
                print(f"{name} movie has been deleted.")
                return
        print(f"{name} movie not found in the list.")


    def list_movie(self):
        if not self.movies:
            print ("No movies in the list.")
            return

        for i in self.movies:
            print(i)


    def filter_movies(self, filter_by, value):
        filtered_movies = []
        if filter_by == "type":
            filtered_movies = [movie for movie in self.movies if movie.type.lower() == value.lower()]
        elif filter_by == "year":
            filtered_movies = [movie for movie in self.movies if movie.year == value]
        else:
            print("Invalid filter type. Use 'type' or 'year' ")
            return

        if not filtered_movies:
            print(f"No movies found for {filter_by}: {value}. ")
            return

        print(f"Movies filtered by {filter_by} '{value}': ")
        for movie in filtered_movies:
            print(movie)

movie_direct = MovieDirector()

print("Welcome to our movie management system.\n"
      "With this system you can create your list by adding movies,\n"
      "then remove the movies you don't want or view which movies you have added by listing them.")

while True:
    print("Choose an option:\n"
          "1. Add movie\n"
          "2. Delete movie\n"
          "3. List all movies\n"
          "4. Filter movies by type or year\n"
          "5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter movie name: ")
        director = input("Enter the director of the movie: ")
        year = input("Enter the year of the movie: ")
        type = input("Enter the movie type: ")
        movie_direct.add_movie(name,director,year,type)
    elif choice == 2:
        name = input("Enter the name of the movie you want to delete: ")
        movie_direct.del_movie(name)
    elif choice == 3:
        print("Movies in the list: ")
        movie_direct.list_movie()
    elif choice == 4:
        filter_by = input("Filter by 'type' or 'year': ").strip().lower()
        value = input(f"Enter the {filter_by} to filter by: ").strip()
        movie_direct.filter_movies(filter_by,value)
    elif choice == 5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Try again.")
