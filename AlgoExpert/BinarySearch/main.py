def binarySearch(array, target):
    # Write your code here. 
    found = 0
    found = map(lambda target:[0] if array[0] == target else -1,array)
    print(found)
    return found

if __name__ == '__main__':
    array = [0,1,21,45,45,61,71,72,73]
    target = 33
    print(binarySearch(array,target))