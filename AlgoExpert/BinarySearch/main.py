def binarySearch(array, target):
    # Write your code here. 
    first_position = 0
    last_position = len(array) - 1

    while first_position <= last_position:
        midpoint_position = first_position + (last_position - first_position) // 2
        midpoint_value = array[midpoint_position] 
        if midpoint_value == target:
            return midpoint_position
        elif target < midpoint_value:
            last_position = midpoint_position -1
        else:
            first_position = midpoint_position + 1
    return -1


if __name__ == '__main__':
    array = [0,1,21,33,45,45,61,71,72,73]
    target = 33
    print(binarySearch(array,target))