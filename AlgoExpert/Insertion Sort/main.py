def insertionSort(array): 
    index_lenght = range(1,len(array))
    for i in index_lenght:
        value_to_sort = array[i]

        while array[i-1] > value_to_sort and i > 0:
            array[i] , array[i-1] = array[i-1] , array[i]
            i -= 1
    return array

if __name__ == '__main__':
    print(insertionSort([3,2,4,5,1,10,0]))