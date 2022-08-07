def filterArray(array):
    final_array = []
    counter = 0
    hash = {}
    for item in array:
        if item in hash and hash[item] == True:
            hash[item] = False
            final_array.append(item)
        else:
            hash[item] = True
            
    return final_array

if __name__ == '__main__':
    array = ["ana", "ana", "ana", "aaa", "aldslaksd", "aaa", "aAa", "ana"]
    result = filterArray(array)
    print(result)