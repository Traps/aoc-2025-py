
import itertools

from . import day02a


def validate_id(id_number:int) -> bool:
    id_digits = str(id_number)
    id_length = len(id_digits)

    min_segment_size = len(set(id_digits))

    for segment_size in range(min_segment_size, id_length // 2 + 1):
        if id_length % segment_size != 0:
            continue
    
        if id_digits.startswith(id_digits[segment_size:]):
            return False
        
    return True


def solve(_input:str) -> int:
    id_values = itertools.chain(*day02a.parse_id_ranges(_input))
    
    return sum(itertools.filterfalse(validate_id, id_values))