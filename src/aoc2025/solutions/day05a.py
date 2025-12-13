
def parse_range(line:str) -> range:
    i,j = map(int, line.split('-'))

    return range(i, j+1)


def parse_databse(_input:str) -> tuple[list[range], list[int]]:
    fresh, available = _input.strip().split('\n\n')

    fresh_ranges = map(parse_range, fresh.splitlines())
    available_ids = map(int, available.splitlines())

    return list(fresh_ranges), list(available_ids)


def solve(_input:str) -> int:
    fresh_ranges, available_ids = parse_databse(_input)

    is_fresh = lambda _id: any(_id in part for part in fresh_ranges)
    
    return sum(map(is_fresh, available_ids))

