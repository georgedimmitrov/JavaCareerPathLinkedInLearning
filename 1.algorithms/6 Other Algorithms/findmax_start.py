# use a recursive algorithm to find a maximum value


# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 111, 41, 49, 53]

def find_max(items):
    # breaking condition: last item in list? return it
    if len(items) == 1:
        return items[0]

    # otherwise get the first item and call function
    # again to operate on the rest of the list
    first = items[0]
    second = find_max(items[1:])

    # perform the comparison when we're down to just two
    if first > second:
        return first
    else:
        return second

# test the function
print(find_max(items))
