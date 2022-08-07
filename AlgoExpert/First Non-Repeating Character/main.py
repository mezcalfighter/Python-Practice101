def firstNonRepeatingCharacter(string):
    # Write your code here.
    array = []
    array[:0] = "".join(string)
    result = -1
    for index in range(len(array)):
        count = array.count(array[index])
        if count == 1:
            result = index
            break 
    return result

if __name__ == '__main__':
    string = "abcdcaf"
    print(firstNonRepeatingCharacter(string))