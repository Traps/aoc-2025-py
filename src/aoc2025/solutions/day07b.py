import functools

from . import day07a


@functools.cache
def get_times_lit(y:int, x:int, emitter_x:int, splitters:frozenset[tuple[int, int]]) -> int:
    if y == 0:
        return int(x == emitter_x)
    
    times_lit = 0
    
    if (y, x-1) in splitters:
        times_lit += get_times_lit(y-1, x-1, emitter_x, splitters)

    if (y, x+1) in splitters:
        times_lit += get_times_lit(y-1, x+1, emitter_x, splitters)

    if (y-1, x) not in splitters:
        times_lit += get_times_lit(y-1, x, emitter_x, splitters)

    return times_lit


def solve(_input:str) -> int:
    splitters = day07a.parse_splitters(_input)
    emitter_x = _input.index('S')

    y_max = max(y for y,_ in splitters)
    x_max = max(x for _,x in splitters)

    last_row = ((y_max + 1, x) for x in range(x_max + 2))

    return sum(get_times_lit(*pos, emitter_x, splitters) for pos in last_row)