def tournamentWinner(competitions, results):
    # Write your code here.
    hash = {}
    winner = " "
    i = 0
    for score in results:
        if score == 1:
            if competitions[i][0] not in hash:
                hash[competitions[i][0]] = 3
                print(hash[competitions[i][0]], "has been created")
            else:
                hash[competitions[i][0]] += 3
        else:
            if competitions[i][1] not in hash:
                print(competitions[i][1])
                hash[competitions[i][1]] = 3
                print(hash[competitions[i][1]], "has been created")
            else:
                hash[competitions[i][1]] += 3
        i += 1
    return max(hash, key=hash.get)

if __name__ == '__main__':
    competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
    results = [0, 0, 1]
    print(tournamentWinner(competitions,results))