from tim_sort import (
insertion_sort,
merge,
tim_sort,
)

from random import shuffle, randint

numbers = list(range(1, 500))
randomized = numbers[:]
shuffle(randomized)

test_data = {
    "sorted": (numbers, numbers),
    "reverse sorted": (list(reversed(numbers)), numbers),
    "randomized": (randomized, numbers),
}

def test_function(function):
    print(f"Testing function {function.__name__}:")
    for key, value in test_data.items():
        result = function(value[0][:])
        print(f"   {key}: {'OK' if result == value[1] else 'ERROR'}")

def test_functions(*functions):
    for function in functions:
        test_function(function)


numbers2 = list(range(1, 100))
numbers3 = list(range(100, 200))
numbers4 = sorted([randint(0, 1000) for x in range(0, 200)])
numbers5 = sorted([randint(0, 1000) for x in range(0, 200)])

merge_test_data = {
    "sequence": (numbers2, numbers3, numbers2 + numbers3),
    "random numbers": (numbers4, numbers5, sorted(numbers4 + numbers5)),
}

def test_merge(function):
    print(f"Testing function {function.__name__}:")
    for key, value in merge_test_data.items():
        result = function(value[0][:], value[1][:])
        print(f"   {key}: {'OK' if result == value[2] else 'ERROR'}")

test_functions(
    tim_sort,
    sorted,
    insertion_sort,
    )

test_merge(merge)