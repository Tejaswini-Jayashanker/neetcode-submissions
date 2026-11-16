class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_nums = {}
        for key in nums:
            if key in dict_nums:
                return True 
            else:
                dict_nums[key] = 1
        return False