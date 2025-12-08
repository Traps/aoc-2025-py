from typing import Generator

def iter_rolls(scroll_map:tuple[str, ...]) -> Generator[tuple[int, int], None, None]:
    for y,row in enumerate(scroll_map):
        yield from ((y,x) for x,c in enumerate(row) if c == '@')


def can_move(scroll_map:tuple[str, ...], y:int, x:int) -> bool:
    n_rolls = 0
    
    for row in scroll_map[max(0, y-1):y+2]:
        n_rolls += row[max(0, x-1):x+2].count('@')

    return n_rolls < 5


def solve(_input:str) -> int:
    rolls = tuple(_input.strip().splitlines())

    return sum(can_move(rolls, *pos) for pos in iter_rolls(rolls))