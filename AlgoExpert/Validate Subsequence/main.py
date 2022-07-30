def isValidSubsequence(array, sequence):
    # Write your code here.
    hash = {}
    i = 0
    temp_list = []
    for index in sequence:
        hash[i] = index
        i += 1
    i = 0
    for index in range(len(array)):
        if i < len(hash):
            if hash[i] == array[index]:
                temp_list.append(array[index])
                i += 1
        else:
            break
    if temp_list == sequence:
        return True
    return False   

if __name__ == '__main__':
    array = [5,1,22,25,6,8,10,-1]
    sequence = [1,6,-1,10]
    print(isValidSubsequence(array,sequence))