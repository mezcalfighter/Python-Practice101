def longestStreakOfAdjacentOnes(array):
    # Write your code here.
    if 0 in array:
        checker = 0
        index = 0
        best_streak = 0
        longest = 1  
        for number in array:
            if checker == 1 or index == len(array)-1:
                if best_streak < longest:
                    best_streak = index
                checker = 0
                longest = 0
            elif number == 0 and checker == 0:
                checker += 1
                index += 1
                longest += 1
            else:
                index += 1
                longest += 1
    else:
        return -1
    return best_streak

if __name__ == '__main__':
    array = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1]
    #array = [1,1,0]
    print(longestStreakOfAdjacentOnes(array))