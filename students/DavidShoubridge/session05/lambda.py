def function_builder(n):

    return [lambda x, c=i: x + c for i in range(n)]


if __name__ == "__main__":
    the_list = function_builder(4)
    assert(the_list[0](2)) == 2
    assert(the_list[1](2)) == 3
