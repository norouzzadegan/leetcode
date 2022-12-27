# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.append(sum(nums[:i+1]))
        return target

