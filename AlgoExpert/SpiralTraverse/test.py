def moveElementToEnd(array, toMove):
    # Write your code here.
    i = 0
    for index in array:
        if index != toMove:
            move = array.pop(i)
            array.insert(0,move)
        i += 1
    return array

if __name__ == '__main__':
    array = [2,1,2,2,2,3,4,2]
    toMove = 2
    new_arr = moveElementToEnd(array,toMove)
    print(new_arr)