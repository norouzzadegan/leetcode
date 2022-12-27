# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.append(sum(nums[:i+1]))
        return target

# https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(i) for i in accounts])

# https://leetcode.com/problems/fizz-buzz/
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        target = []
        for i in range(1, n+1):
            if (i % 5 == 0) and (i % 3 == 0):
                target.append('FizzBuzz')
            elif (i % 3 == 0):
                target.append('Fizz')
            elif (i % 5 == 0):
                target.append('Buzz')
            else:
                target.append(str(i))
        return target