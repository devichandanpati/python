def double_stuff(values) :
    """ Returns a new list which contains the double of the elements in the list values """
    new_list = []
    for value in values :
        new_elem = 2 * values
        new_list.append(new_elem)
    return new_list
things = [2,5,9]
more_things = double_stuff(things)
print(things)
print(more_things)

