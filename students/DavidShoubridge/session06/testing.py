def arithmetic(x):
    """
    Will py.test go through sub-directories to find files to test? Yup it will!
    """
    return x - 4


def test_arithmetic():
    assert(arithmetic(4) == 0)
