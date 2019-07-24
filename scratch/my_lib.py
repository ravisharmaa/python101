def print_length_of_the_name(name):
    return len(name)


def print_the_name_it_self(name):
    return name


if __name__ == 'main':
    my_name = 'Ravi'
    length = print_length_of_the_name(my_name)
    print(length)

    name_from_the_function = print_the_name_it_self(my_name)
    print(name_from_the_function)


