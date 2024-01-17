def find_max_min(int_array):
    max = None
    min = None
    for x in int_array:
        if max == None or x > max:
            max = x
        if min == None or x < min:
            min = x
    return [min, max]


print('Hello! Welcome to Max & Min, I will find the max and min number of a list of integers that you provide!')
string_input = input(
    'Please provide the list of integers, please separate the integers by spaces:\n')
int_array = list(map(int, string_input.split()))

print('[min, max] of your array =', find_max_min(int_array))
