import argparse
import importlib
import pathlib
import time

from typing import Any, Callable

from . import inputs


def simple_timit(callable:Callable, *args:Any, **kwargs:Any) -> tuple[float, Any]:
    t_start = time.perf_counter()

    result = callable(*args, **kwargs)

    t_end = time.perf_counter()

    return (t_end - t_start, result) 


def main() -> None:
    parser = argparse.ArgumentParser('aoc2025')

    parser.add_argument('day', type=int, choices=range(1,13))
    parser.add_argument('part', type=str, choices=('a', 'b'), default=('a', 'b'), nargs='?')
    parser.add_argument('-s', '--sample', action='store_true')
    parser.add_argument('-c', '--challenge', action='store_true')
    parser.add_argument('-f', '--file', type=str)
    
    args = parser.parse_args()

    challenge_input = None
    
    for part in args.part:
        print(f'Part {part.upper()}:')
        try:
            task_module = importlib.import_module(f'.solutions.day{args.day:02d}{part}', 'aoc2025')
        except ModuleNotFoundError:
            print(f'  Module not found.')
            continue

        if args.sample or (not args.challenge and not args.file):
            try:
                sample_inputs = inputs.get_sample_inputs(args.day, part)
            except KeyError:
                print(f'  No sample inputs found.')
                sample_inputs = ()

            for i,sample in enumerate(sample_inputs, 1):
                run_time, result = simple_timit(task_module.solve, sample)

                print(f'  Sample {i} answer: {result} (run time: {run_time:.3f}s)')

        if args.challenge or (not args.sample and not args.file):
            if challenge_input is None:
                challenge_input = inputs.get_challenge_input(args.day)

            run_time, result = simple_timit(task_module.solve, challenge_input)

            print(f'  Challenge answer: {result} (run time: {run_time:.3f}s)') 
        
        if args.file:
            src_file = pathlib.Path(args.file)

            try:
                file_content = src_file.read_text('utf-8')
            except FileNotFoundError:
                print(f'  Specified file not found: \'{src_file}\'')
            except UnicodeDecodeError:
                print(f'  Input file content could not be decoded, expected UTF-8.')
            else:
                run_time, result = simple_timit(task_module.solve, file_content)

                print(f'  File input answer: {result} (run time: {run_time:.3f}s)') 


if __name__ == '__main__':
    main()