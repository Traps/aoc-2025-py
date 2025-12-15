import operator
import itertools

from typing import Callable, Generator

from .day06a import solve_problem


def pivot_value_rows(value_rows:list[str]) -> Generator[list[int]]:
    columns = map(''.join, zip(*value_rows, strict=True))

    while values := list(itertools.takewhile(str.strip, columns)):
        yield list(map(int, values))


def parse_homework(_input:str) -> tuple[list[Callable], list[list[int]]]:
    *values, ops = _input.splitlines()

    columns = pivot_value_rows(values)

    ops = [operator.add if op == '+' else operator.mul for op in ops.split()]

    return ops, list(columns)


def solve(_input:str) -> int:
    ops, columns = parse_homework(_input)

    return sum(solve_problem(*problem) for problem in zip(ops, columns))