def twoNumberSum(array, targetSum):
    # Write your code here.
    hash = {}
    for item in array:
        hash[item] = True
    for item in array:
        temp_value = targetSum - item
        print(item)
        if item != temp_value and temp_value in hash:
            return [item,temp_value]
            #result.append([item,temp_value])
    return []

#This is the main function
if __name__ == '__main__':
    array = [3,5,-4,8,11,1,-1,6]
    targetSum = 10
    found = twoNumberSum(array,targetSum)
    print(found)