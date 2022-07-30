def threeNumberSum(array, targetSum):
    array.sort(reverse=False)
    result = []
    hash = {}
    #Build hashmap
    for item in array:
        hash[item] = True
    for item in array:
        for item2 in array:
            if item != item2:
                to_find = targetSum - (item + item2)
                if to_find != item and to_find != item2 and to_find in hash:
                    hit = [item,item2,to_find]
                    hit.sort(reverse=False)
                    if not hit in result:
                        result.append(hit)
    return result



        

if __name__ =='__main__':
    array = [-8,-6,1,2,3,5,6,12]
    targetSum = 0
    resultFunc = threeNumberSum(array,targetSum)
    print(resultFunc)