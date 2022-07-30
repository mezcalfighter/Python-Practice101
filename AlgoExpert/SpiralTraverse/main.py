temp_arr = []

def spiralTraverse(array):
    # Write your code here.
    for item in array:
        temp_arr.extend(item)
    print(temp_arr)
    return temp_arr.sort(reverse=False)

if __name__ == '__main__':
    array = [
        [1,2,3,4],
        [12,13,14,5],
        [11,16,15,6],
        [10,9,8,7],
    ]
    spiralTraverse(array)
    print(temp_arr)