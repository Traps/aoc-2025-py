import functools


@functools.cache
def is_lit(y:int, x:int, emitter_x:int, splitters:frozenset[tuple[int, int]]) -> bool:
    if y == 0:
        return x == emitter_x
    
    if (y, x-1) in splitters and is_lit(y-1, x-1, emitter_x, splitters):
        return True

    if (y, x+1) in splitters and is_lit(y-1, x+1, emitter_x, splitters):
        return True

    return (y-1, x) not in splitters and is_lit(y-1, x, emitter_x, splitters)


def parse_splitters(_input:str) -> frozenset[tuple[int, int]]:
    width = _input.index('\n')

    manifold = enumerate(_input.replace('.' * width + '\n', ''))

    return frozenset(divmod(i, width+1) for i,c in manifold if c == '^')


def solve(_input:str) -> int:
    splitters = parse_splitters(_input)
    emitter_x = _input.index('S')

    return sum(is_lit(*pos, emitter_x, splitters) for pos in splitters)