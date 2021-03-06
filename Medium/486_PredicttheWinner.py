"""
Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:

Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return False.
Example 2:

Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
Note:

1 <= length of the array <= 20.
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.
"""

class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        return self.canWin(nums, 0, 0, 1)
    
    def canWin(self, nums, sum1, sum2, player):
        if len(nums) == 0:
            return sum1 >= sum2
        if len(nums) == 1:
            return sum1 + nums[0] >= sum2 if player == 1 else sum2 + nums[0] > sum1
        if player == 1:
            return not self.canWin(nums[1:], sum1 + nums[0], sum2, 2) or not self.canWin(nums[:-1], sum1 + nums[-1], sum2, 2)
        if player == 2:
            return not self.canWin(nums[1:], sum1, sum2 + nums[0], 1) or not self.canWin(nums[:-1], sum1, sum2 + nums[-1], 1)
        """
        n = len(nums)
        if n % 2 == 0 or n == 1:
            return True
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for k in range(1, n):
            for i, j in zip(range(n), range(k, n)):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][n - 1] >= 0
        