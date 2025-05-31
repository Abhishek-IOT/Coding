"""
Problem Link : https://leetcode.com/problems/two-sum/


Intiution : As a+b=t we will make this as a=b-t and check value of a in Map if found we wil return the index.

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in d:
                return [d[diff],i]
            d[nums[i]]=i
        return [-1,-1]

        

