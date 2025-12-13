from typing import Iterable

from . import day05a


def range_unity(r0:range, r1:range) -> list[range]:
    if (r0.stop - 1) in r1 or (r1.stop - 1) in r0:
        return [range(min(r0.start, r1.start), max(r0.stop, r1.stop))]
    
    return [r0, r1]


def dissolve_intersecting_ranges(parts:Iterable[range]) -> list[range]:
    parts = sorted(parts, key=lambda r: r.start)

    dissolved = [parts.pop(0)]

    for part in parts:
        dissolved.extend(range_unity(dissolved.pop(), part))

    return dissolved


def solve(_input:str) -> int:
    fresh_ranges, _ = day05a.parse_databse(_input)

    dissolved_ranges = dissolve_intersecting_ranges(fresh_ranges)

    return sum(map(len, dissolved_ranges))