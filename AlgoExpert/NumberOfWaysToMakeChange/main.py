def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    hash = {}
    total = 0
    amounts = []
    temp_amount = []
    generated_amount = 0
    i = 0
    new_denoms = [index for index in denoms if index <= n]
    for index in range(n):
        if i == len(new_denoms)-1:
            break
        elif generated_amount == n:
            if temp_amount not in amounts:
                total += 1
        elif new_denoms[i] + generated_amount < n:
            if generated_amount[i] + generated_amount[i+1] <= n:
                
    return total

if __name__ == '__main__':
    #denoms = [1,5,10,25]
    denoms = [1,5]
    n = 4
    # count = 
    numberOfWaysToMakeChange(n,denoms)
    # print(count)