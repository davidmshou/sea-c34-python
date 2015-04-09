import series


def test_fibonacci():
    assert(series.fibonacci(1) == 1)
    assert(series.fibonacci(5) == 5)
    assert(series.fibonacci(7) == 13)


def test_lucas():
    assert(series.lucas(0) == 2)
    assert(series.lucas(3) == 4)
    assert(series.lucas(7) == 29)
