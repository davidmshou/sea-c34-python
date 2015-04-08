# def syntax-error(x, y):
#     print(x + y)


def name_error(name):
    print name


x = 2
y = "3"


def type_error(x, y):
    print x + y


def attribute_error():
    print(attribute_error.min)

if __name__ == '__main__':

    # syntax-error(2, 2)
    name_error(name)
    type_error(x, y)
    attribute_error()
