def nonConstructibleChange(coins):
    coins.sort()
    minimum = 0
    for coin in coins:
        if coin > minimum + 1:
            break
        minimum += coin
    return (minimum + 1)


#This is the main function
if __name__ == '__main__':
    #coins = [5, 7, 1, 1, 2, 3, 22]
    coins = [1,2,1,5]
    found = nonConstructibleChange(coins)
    print(found)
