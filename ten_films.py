from create_table import create_table
from colorama import init,Fore,Back
from mysql.connector.cursor import MySQLCursor
from typing import Union
from typing import List, Tuple
from choice import make_choice

def year_films_10(csr: MySQLCursor, sel_year: int, sign: Union[int, float]) -> List[Tuple[int, str, set]]:
    print(sel_year, sign)
    csr.execute(
        f"""  select title, genres,year, cast, directors,`imdb.rating`, languages,runtime, plot
        from movies
        where year {sign} {sel_year}
        order by `imdb.rating` desc
        limit 10
        """
    )
    print(Fore.LIGHTMAGENTA_EX + " A selection of besten 10 movies:\n")
    for film in csr.fetchall():
        print(*film, sep="\n\t",end="\n\n")

def category_films_10(csr: MySQLCursor, gen: str)-> List[Tuple[int, str, set]]:
    csr.execute(
        f"""  select title, genres,year, cast, directors,`imdb.rating`, languages,runtime, plot
        from movies
        where genres like "{gen}"
        order by `imdb.rating` desc
        limit 10
        """
    )
    films = csr.fetchall()

    if len(films) == 0:
        print("Nothing was found for your request.")
    else:
        print(Fore.LIGHTMAGENTA_EX +" A selection of besten 10 movies:\n")

    for film in films:
        print(*film, sep="\n\t", end="\n\n")

def actor_films_10(csr: MySQLCursor, sel_actor: str) -> List[Tuple[int, str, set]]:
    csr.execute("select title, genres,year, cast, directors,`imdb.rating`, languages,runtime, plot from movies where cast like \"%"+sel_actor+"%\" order by `imdb.rating` desc limit 10")
    films = csr.fetchall()

    if len(films) == 0:
        print("Nothing was found for your request.")
    else:
        print(Fore.LIGHTMAGENTA_EX +" A selection of besten 10 movies:\n")

    for film in films:
        print(*film, sep="\n\t",end="\n\n")

def director_films_10(csr: MySQLCursor, dir: str) -> List[Tuple[int, str, set]]:
    csr.execute(
        "select title, genres, year, cast, directors,`imdb.rating`, languages,runtime, plot from movies where directors like \"%"+dir+"%\" order by `imdb.rating` desc limit 10")
    
    films = csr.fetchall()

    if len(films) == 0:
        print("Nothing was found for your request.")
    else:
        print(Fore.LIGHTMAGENTA_EX +" A selection of besten 10 movies:\n")

    for film in films:
        print(*film, sep="\n\t",end="\n\n")

def pop_query_result(cst: MySQLCursor) -> List[Tuple[int, str, set]]:
    my_queries = ['Actor', 'Director', 'Year', 'Genres',  'Word']
    pop = make_choice( Fore.GREEN + f"Enter {my_queries} \n", my_queries )

    cst.execute("select result, count(result) from pop_searches where request like \"%"+pop+"%\" GROUP BY result ORDER BY count(result) desc")
    
    pop_result = cst.fetchall()
    print( create_table( ["Result", "Count"], pop_result ) )
    
    return pop_result