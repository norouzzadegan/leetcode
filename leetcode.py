def runningSum(nums):
    target = []
    for i in range(len(nums)):
        target.append(sum(nums[:i+1]))
    return target