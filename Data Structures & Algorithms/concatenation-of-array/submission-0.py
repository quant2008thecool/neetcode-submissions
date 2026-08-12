class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

# nums = length is n 
# ans = length is 2n 
# ans[i] should be equal to nums[i]
# and nums[i+1] == nums[i]
        return nums+nums