import fresh_tomatoes
import webbrowser
import media

# These are the objects of movie class
Movie1 = media.Movie("12 Monkeys",
                     "http://bit.ly/2uKjsZY",
                     "https://www.youtube.com/watch?v=15s4Y9ffW_o")
Movie2 = media.Movie("A Beautiful Mind",
                     "http://bit.ly/2w35D8E",
                     "https://www.youtube.com/watch?v=YWwAOutgWBQ")
Movie3 = media.Movie("Being Human",
                     "http://bit.ly/2v3ex1C",
                     "https://www.youtube.com/watch?v=7_Xe2RBNgfI")
Movie4 = media.Movie("City Lights",
                     "http://bit.ly/2fMhtxB",
                     "https://www.youtube.com/watch?v=b2NTUnujk1I")
Movie5 = media.Movie("Daredevil",
                     "http://bit.ly/2v3zCJ3",
                     "https://www.youtube.com/watch?v=dlbEZFEt5-0")
Movie6 = media.Movie("Elf",
                     "http://bit.ly/2wREiUI",
                     "https://www.youtube.com/watch?v=gW9wRNqQ_P8")
# movies is a list of all the objects of a movie class
movies = [Movie1, Movie2, Movie3, Movie4, Movie5, Movie6]
# this is a function call from a function in fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
