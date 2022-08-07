def findThreeLargestNumbers(my_array):
    compare_array = my_array
    longest_values = []
    print("Array: {} Copy: {}".format(my_array,compare_array))
    longest_values = map(filterArray,longest_values,my_array)
    longest_values = list(longest_values)
    return longest_values


if __name__ == '__main__':
    my_array = [7,7,7,7,7,7,7,7,7,7,7]
    print(findThreeLargestNumbers(my_array))