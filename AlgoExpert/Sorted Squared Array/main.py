def squared(n):
    return n * n

def sortedSquaredArray(array):
    # Write your code here.
    new_array = list(map(squared,array))
    new_array.sort(reverse=False)
    return new_array

if __name__ == '__main__':
    array = [1,2,3,5,6,8,9]
    print(sortedSquaredArray(array))