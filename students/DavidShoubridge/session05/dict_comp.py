from __future__ import print_function

"""Task1"""


def print_string():
    """
    Print a string using string formatting and the food_prefs dict.
    """
    food_prefs = {u"name": u"David",
                  u"city": u"Seattle",
                  u"cake": u"chocolate",
                  u"fruit": u"kiwi",
                  u"salad": u"caesar",
                  u"pasta": u"pizza"}

    print(
        u"{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta.".format(**food_prefs)
    )
"""Task2"""


def zip_lists():
    """
    Creates a dict from 2 lists and then prints.
    """
    numbers = [number for number in range(0, 16)]
    letters = [hex(number) for number in (range(16))]

    num_letter = dict(zip(numbers, letters))

    print(num_letter)


"""Task 3"""


def dict_comp():
    """
    Recreates the above dict using only dict comprehension.
    """
    num_letter = {num: hex(num) for num in range(16)}
    print(num_letter)

"""Task4"""


def num_a():
    """
    Prints dictionary with the same keys as food_prefs but with the number of \
    'a's in each value as the value.
    """
    food_prefs = {u"name": u"David",
                  u"city": u"Seattle",
                  u"cake": u"chocolate",
                  u"fruit": u"kiwi",
                  u"salad": u"caesar",
                  u"pasta": u"pizza"}

    number_a = {key: value.count('a') for key, value in food_prefs.items()}
    print(number_a)

"""Task5"""


def set_comp():
    numbers = range(0, 21)

    s2 = {number for number in numbers if number % 2 == 0}
    s3 = {number for number in numbers if number % 3 == 0}
    s4 = {number for number in numbers if number % 4 == 0}
    print(s2, s3, s4)

if __name__ == "__main__":
    print_string()
    zip_lists()
    dict_comp()
    num_a()
    set_comp()
