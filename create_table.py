from prettytable import PrettyTable
from typing import List

def create_table( names: List[str], columns: List ) -> PrettyTable:
    table = PrettyTable()
    table.field_names = list(names)
    for q in columns:
        table.add_row( q )
        
    return table 