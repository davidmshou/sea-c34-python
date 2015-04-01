from __future__ import print_function


def count_evens(nums):
    evens += [1 for number in nums if number % 2 == 0]
    return evens


if __name__ == "__main__":
    print(count_evens([2, 1, 2, 3, 4]))
    print(count_evens([2, 2, 0]))
    print(count_evens([1, 3, 5]))
