import itertools

from typing import Generator


def parse_id_ranges(_input:str) -> Generator[range, None, None]:
    for limits in _input.strip().split(','):
        start, stop = map(int, limits.split('-'))

        yield range(start, stop+1)


def validate_id(id_number:int) -> bool:
    id_digits = str(id_number)
    id_length = len(id_digits)
    
    return id_length % 2 != 0 or id_digits[:id_length//2] != id_digits[id_length//2:]


def solve(_input:str) -> int:
    id_values = itertools.chain(*parse_id_ranges(_input))

    return sum(itertools.filterfalse(validate_id, id_values))