import functools

from . import day01a


def update_dial_state(prev_state:tuple[int, int], rotation:int) -> tuple[int, int]:
    zero_count, prev_pos = prev_state

    n_cross, new_pos = divmod(prev_pos + rotation, 100)

    if rotation < 0:
        n_cross = max(0, abs(n_cross) - (prev_pos == 0)) + (new_pos == 0)
        
    return (zero_count + abs(n_cross), new_pos)


def solve(_input:str) -> int:
    rotations = day01a.parse_rotations(_input)

    zero_count, _ = functools.reduce(update_dial_state, rotations, (0, 50))

    return zero_count