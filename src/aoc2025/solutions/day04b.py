from typing import TypeAlias

from . import day04a

YXPos:TypeAlias = tuple[int, int]

        
def get_neighbours(rolls:set[YXPos], y:int, x:int) -> set[YXPos]:
    return {(y-1,x-1),(y-1,x),(y-1,x+1),(y,x-1),(y,x+1),(y+1,x-1),(y+1,x),(y+1,x+1)} & rolls


def _remove_loose_rolls(rolls:set[YXPos], _candidates:set[YXPos]|None=None) -> None:
    new_candidates = set()
    removed = set()
    
    for pos in (_candidates or rolls):
        if len(neighbours := get_neighbours(rolls, *pos)) >= 4:
            continue

        new_candidates.update(neighbours)
        removed.add(pos)
    
    rolls -= removed
    new_candidates -= removed

    if new_candidates:
        return _remove_loose_rolls(rolls, new_candidates)


def remove_loose_rolls(rolls:set[YXPos]) -> set[YXPos]:
    blocked_rolls = set(rolls)

    _remove_loose_rolls(blocked_rolls)

    return blocked_rolls


def solve(_input) -> int:
    all_rolls = set(day04a.iter_rolls(_input.strip().splitlines()))

    blocked_rolls = remove_loose_rolls(all_rolls)

    return len(all_rolls) - len(blocked_rolls)