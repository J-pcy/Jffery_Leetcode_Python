"""
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
"""

class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = [0] * len(nums) 
        scoredict = {}
        for i in range(len(nums)):
            scoredict[i] = nums[i]
        rank = sorted(scoredict, key = lambda x:scoredict[x], reverse = True)
        for i in range(len(rank)):
            if i == 0:
                res[rank[i]] = "Gold Medal"
            elif i == 1:
                res[rank[i]] = "Silver Medal"
            elif i == 2:
                res[rank[i]] = "Bronze Medal"
            else:
                res[rank[i]] = str(i + 1)
        return res
    