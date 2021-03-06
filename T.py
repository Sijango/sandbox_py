def find_index(value, items):
    for index, item in enumerate(items):
        if item == value:
            return index


# BEGIN (write your solution here)
def find_second_index(value, items):
    if not items:
        return None
    cursor = iter(items)
    first_index = find_index(value, cursor)
    second_index = find_index(value, cursor)
    print(second_index)
    if not second_index and second_index != 0:
        return None
    return first_index + second_index + 1
# END


print(find_second_index('n', 'cannon'))