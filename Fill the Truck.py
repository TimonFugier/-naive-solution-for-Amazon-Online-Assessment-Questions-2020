def fillTheTruck(num: int, boxes: List[int], unitSize: int, unitsPerBox: List[int], truckSize: int) -> int:
    totalArray = []
    for i in range(num):
        for j in range(boxes[i]):
            totalArray.append(unitsPerBox[i])
    totalArray.sort()
    total = 0
    for i in range(truckSize):
        if len(totalArray)-i-1 >=0 :
            total += totalArray[len(totalArray)-i-1]
    return total
