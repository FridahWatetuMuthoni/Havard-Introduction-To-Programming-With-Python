

def array_of_range(start, end):
    if (start > end):
        return []
    numbers = array_of_range(start, end-1)
    numbers.append(end)
    return numbers


print(array_of_range(1, 10))
