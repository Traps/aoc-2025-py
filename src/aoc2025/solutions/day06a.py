import operator
import functools

from typing import Callable


def parse_homework(_input:str) -> tuple[list[Callable], list[list[int]]]:
    *values, ops = map(str.strip, _input.strip().splitlines())

    columns = zip(*(map(int, line.split()) for line in values))

    ops = [operator.add if op == '+' else operator.mul for op in ops.split()]

    return ops, list(columns)


def solve_problem(op:Callable[[int, int], int], values:list[int]) -> int:
    return functools.reduce(op, values[1:], values[0])


def solve(_input:str) -> int:
    ops, columns = parse_homework(_input)

    return sum(solve_problem(*problem) for problem in zip(ops, columns))