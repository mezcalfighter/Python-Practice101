def bubbleSort(unsorted_array):
    index_lenght = len(unsorted_array) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0,index_lenght):
            if unsorted_array[i] > unsorted_array[i+1]:
                sorted = False
                unsorted_array[i] , unsorted_array[i+1] = unsorted_array[i+1] , unsorted_array[i]
    return unsorted_array

if __name__ == '__main__':
    print(bubbleSort([4,6,8,3,9,10,1,3]))