import math



class debtRecord:
    borrower = ""
    lender = ""
    amount = 0

    def __init__(self, borrower, lender, amount):
        self.borrower = borrower
        self.lender = lender
        self.amount = amount


def minimumDebtMembers(records: List[debtRecord]) -> List[str]:
    dic = {}
    for i in range(len(records)):
        if records[i].borrower in dic:
            dic[records[i].borrower] -= records[i].amount
        else:
            dic.update({records[i].borrower: -records[i].amount})
        if records[i].lender in dic:
            dic[records[i].lender] += records[i].amount
        else:
            dic.update({records[i].lender: records[i].amount})

    mini = math.inf
    for cle, valeur in dic.items():
        if valeur < mini:
            mini = valeur

    if mini >= 0:
        return ["Nobody has a negative balance"]
    resultString = []
    for cle, valeur in dic.items():
        if valeur == mini:
            resultString.append(cle)

    resultString.sort()
    return resultString
