def processLogFile(logs, threshold):
    """
    :type logs: List[str]
    :type threshold: int
    :rtype: List[str]
    """
    amount = []
    users = []
    for i in range(len(logs)):
        a, b, c = logs[i].split(" ")
        if (a == b):
            if (a in users):
                index = users.index(a)
                amount[index] += 1
            else:
                users.append(a)
                amount.append(1)
        else:
            if (a in users):
                index = users.index(a)
                amount[index] += 1
            else:
                users.append(a)
                amount.append(1)
            if (b in users):
                index = users.index(b)
                amount[index] += 1
            else:
                users.append(b)
                amount.append(1)

    returnedArray = []
    for i in range(len(amount)):
        if amount[i] >= threshold:
            returnedArray.append(users[i])
    returnedArray.sort()
    return returnedArray
