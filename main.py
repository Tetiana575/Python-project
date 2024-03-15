from db import DataBase
from choice import *
from ten_films import *
from select_ import *
from create_table import *
from colorama import init, Fore, Back

my_db = DataBase()

cursor = my_db.cursor
connection = my_db.connection
cursor_right = my_db.cursor_right
my_connection = my_db.my_connection

init(autoreset = True)# для работы колорамы

def insert_data(cst, my_con, params, sel_list):
    data = {"request": params, "result": sel_list}
    cst.execute("INSERT INTO pop_searches (request, result) VALUES (%(request)s, %(result)s)", data)
    my_con.commit()

def new_request() -> bool:
    yn = ["yes","no"]
    n = input(Fore.LIGHTMAGENTA_EX +f"Want to continue?\n {yn}\t").strip().lower()
    if n == "no":
        cursor.close()
        connection.close()
        return False
    return True

def my_quieres()-> None:
    my_category: List[str] = ['Actor', 'Director', 'Year', 'Genres', 'Genres and year', 'Word', 'Pop queries', 'Exit']
    is_closed: bool = False
    while not is_closed:
        choice: str = input(Fore.LIGHTGREEN_EX + f" Welcome to our portal.\n Here you will find movies for every taste. \n We will select for you 10 movies with the highest rating.\n\n Select a search creterion: \n{my_category}\n").lower()
        if choice == "genres":
            result = select_category(cursor)
            gen = make_choice( f'Enter genre:\n {result}\n', result )
            category_films_10(cursor,gen)
            insert_data(cursor_right, my_connection, choice, gen)
        elif choice == "year":
            years = select_year(cursor)
            sel_year = make_choice( f'Select year: \n {years}\n', years )
            sign = make_choice( "Enter a greater\n <,>,=,<=,>= :\t", ["<",">",">=","<=","="] )
            
            year_films_10(cursor, int(sel_year), sign)
            insert_data(cursor_right, my_connection, choice, sel_year)#функция записи
        elif choice == "genres and year":
            genres, years = select_genres_year(cursor)
            gen = input(f"Input genres:\n ({genres}):\n")
            year = int(input(f"Input year:\n ({years}):\n "))
            films_by_genre_and_year(cursor, gen, year)
            insert_data(cursor_right, my_connection, choice, gen + " " + str(year))
        elif choice == "actor":
            sel_actor = input(f'Enter actor name: \n').strip().capitalize()
            actor_films_10(cursor,sel_actor)
            insert_data(cursor_right, my_connection, choice, sel_actor)
        elif choice == "director":
            dir = input(f'Enter director name: \n').strip().capitalize()
            director_films_10(cursor,dir)
            insert_data(cursor_right,my_connection,choice,dir)
        elif choice == "pop queries":
            pop_queries(cursor_right)    
            pop_query_result(cursor_right)
        elif choice == "word":
            key_word = select_key_word(cursor)
            insert_data(cursor_right, my_connection, choice, key_word)
        elif choice == "exit":
            my_db.disconnect()
            break
        else:
            choice = input(Fore.LIGHTGREEN_EX + f"Select a search creterion:\n {my_category}\n").lower()

        is_closed = not new_request()

if __name__ == "__main__":
    my_quieres()