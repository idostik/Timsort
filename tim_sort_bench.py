from tim_sort import (
merge,
insertion_sort,
tim_sort,
)

from random import shuffle
from timeit import repeat

def create_test_data(count):
    numbers = list(range(1, count + 1))
    randomized = numbers[:]
    shuffle(randomized)

    return {
        f"{count:7d} sorted": numbers,
        f"{count:7d} reverse sorted": list(reversed(numbers)),
        f"{count:7d} randomized": randomized
    }


def benchmark_function(function, test_data):
    print(f"Benchmarking function {function.__name__}")
    for data in test_data.values():
        for key, value in data.items():
            command = f"{function.__name__}({value})"
            time = min(repeat(command, number=1, repeat=3, globals=globals()))
            print(f"    {key}: {time:.7f} s", end="\t")
        print()

def benchmark_functions(test_data, *functions):
    for function in functions:
        benchmark_function(function, test_data)


test_data = {}
for count in (10, 100, 1_000, 5_000, 10_000, 50_000, 100_000, 200_000, 500_000, 1_000_000):
    test_data[count] = create_test_data(count)

benchmark_functions(
    test_data,
    #sorted,
    tim_sort,
    )