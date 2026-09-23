class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sortlist=sorted(nums)
        for i in range(len(sortlist)-1): 
            if sortlist[i]==sortlist[i+1]:
                return True 
        return False