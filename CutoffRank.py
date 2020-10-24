# SLOW
"""
def countLevelUpPlayers(cutOffRank, num, scores):
    scores.sort()
    res = 0
    if cutOffRank == 0:
        return 0
    for i in range(num):

        if scores[num - 1 - i] > 0 and i < cutOffRank - 1:
            res += 1

        elif (scores[num - 1 - i] == scores[num - 1 - cutOffRank + 1]):
            res += 1

    return res
"""

# Correct

def countLevelUpPlayers(cutOffRank, num, scores):
    scores.sort()
    if cutOffRank == 0:
        return 0
    res = cutOffRank
    if (scores[num - cutOffRank] == 0):
        counter = 0
        while num - cutOffRank + counter < num and scores[num - cutOffRank + counter] == 0:
            counter += 1
            res -= 1
        return res

    i = cutOffRank
    while ((num - 1 - i) >= 0 and scores[num - 1 - i] == scores[num - cutOffRank]):
        res += 1
        i += 1

    return res
