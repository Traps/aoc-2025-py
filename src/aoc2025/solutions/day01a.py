import itertools

from typing import Generator


def parse_rotations(_input:str) -> Generator[int, None, None]:
    for line in _input.strip().splitlines():
        yield int(line[1:]) * (1 if line[0] == 'R' else -1)


def solve(_input:str) -> int:
    rotations = parse_rotations(_input)
    
    dial_positions = itertools.accumulate(
        rotations, lambda a,r: (a + r) % 100, initial=50
    )

    return sum(p == 0 for p in dial_positions)