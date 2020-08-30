def double_stuff(values) :
    """
    Returns new list which contains
    double the values in the old list
    """
    new_list = []
    for value in values :
        new_elem = 2 * value
        new_list.append(new_elem)

    return new_list
new_list = [2,5,9]
more_things = double_stuff(new_list)
print(new_list)
print(more_things)

