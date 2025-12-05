from typing import Generator

def iter_scrolls(scroll_map:tuple[str, ...]) -> Generator[tuple[int, int], None, None]:
    for y,row in enumerate(scroll_map):
        yield from ((y,x) for x,c in enumerate(row) if c == '@')


def can_move(scroll_map:tuple[str, ...], y:int, x:int) -> bool:
    n_scrolls = 0
    
    for row in scroll_map[max(0, y-1):y+2]:
        n_scrolls += row[max(0, x-1):x+2].count('@')

    return n_scrolls < 5


def solve(_input:str) -> int:
    scroll_map = tuple(_input.strip().splitlines())

    return sum(can_move(scroll_map, *pos) for pos in iter_scrolls(scroll_map))