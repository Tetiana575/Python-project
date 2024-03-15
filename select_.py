from create_table import create_table
from mysql.connector.cursor import MySQLCursor
from colorama import init,Fore,Back
from typing import List, Tuple

def select_genres_year(csr: MySQLCursor) ->List[Tuple[int, str, set]]:
    csr.execute("select group_concat(genres) from movies")
    
    l = csr.fetchall()[0][0].split(',')#из списка кортежей делаем список, разделаем список
    list_genres = list(set(l))#делаем множество уникальных      
    
    csr.execute("SELECT DISTINCT year FROM movies")

    list_year = [ line[0] for line in csr.fetchall() ]

    return list_genres, list_year

def select_year(csr: MySQLCursor) -> list[int]:
    csr.execute("SELECT DISTINCT year FROM movies")

    return [ line[0] for line in csr.fetchall() ]
    
def select_category(csr: MySQLCursor) ->set:
    csr.execute("select group_concat(genres) from movies")
    l = csr.fetchall()[0][0]#из списка кортежей делаем список
    result = list(set(l.split(',')))#разделаем список, делаем множество уникальных
    return result

def select_key_word(csr: MySQLCursor) -> List[Tuple[int, str, set]]:
    key_word = input(Fore.LIGHTGREEN_EX + "Insert key word:\t").strip().lower()
    csr.execute("select title, genres,year, cast, directors,`imdb.rating`, languages,runtime, plot from movies where title like \"%"+key_word+"%\" limit 10")
    films = csr.fetchall()

    if len(films) == 0:
        print(Fore.LIGHTMAGENTA_EX + "Nothing was found for your request.")
    else:
        print(Fore.LIGHTMAGENTA_EX + " A selection of besten 10 movies:\n")

    for film in films:
        print(*film, sep="\n\t",end="\n\n")
            
    return key_word

def pop_queries(cst: MySQLCursor) -> List[Tuple[int, str]]:
    cst.execute("""SELECT request, count(request)  FROM pop_searches GROUP BY request ORDER BY count(request) desc """)
    query = cst.fetchall()
    table = create_table( [ "Request name", "count" ], query )
    print(Fore.LIGHTGREEN_EX + "Popular queries:\n")
    print( table )
    return query 

def films_by_genre_and_year(cursor: MySQLCursor, genre: str, year: int) -> List[Tuple[int, str, set]]:
    cursor.execute(
        f"""SELECT title, genres, year, runtime, cast, directors, 'imdb.rating', languages, plot 
            FROM movies 
            WHERE genres LIKE '%{genre}%' AND year = {year} 
            ORDER BY 'imdb.rating' DESC LIMIT 10"""
    )
    films = cursor.fetchall()
    print(Fore.LIGHTMAGENTA_EX +" A selection of besten 10 movies:\n")
    for film in films:
        print(*film, sep="\n\t",end="\n\n")