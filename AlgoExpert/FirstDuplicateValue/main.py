def firstDuplicateValue(array):
    # Write your code here.
    # Creates a hashmap empty
    hash = {}
    for item in array:
        print(hash)
        #Takes item and looks for an key with that value
        if hash.get(item):
            #If found
            return item
        #If not found adds that item to dict
        hash[item] = True
    return -1

if __name__ == '__main__':
    #array = [2,1,5,2,3,3,4]
    array = [2,1,5,3,3,2,4]
    print(firstDuplicateValue(array))