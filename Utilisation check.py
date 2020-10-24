import math
def finalInstances(instances, averageUtil):
    """
    :type instances: int
    :type averageUtil: List[int]
    :rtype: int
    """
    i = 0
    while i < len(averageUtil):
        if averageUtil[i]< 25 :
            if instances >1 :
                instances = math.ceil(instances/2)
                i += 10
        elif averageUtil[i] > 60 :
            if instances<=10^8 :
                instances = instances * 2
                i += 10
        else:
            i += 1
    return instances
