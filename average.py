def average(items):

    if len(items) == 0:
        raise(ValueError("The list is empty."))

    temp = 0
    for x in items:
        temp += x
    return temp / len(items)

