from typing import List



def make_choice( text: str, variation: List[str]) -> str:
    variation = list(map( str, variation ))
    ans = input( text ).strip().capitalize()
    while ans not in variation:
        ans = input( text )
    return ans