class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)): 
            num = nums[i]
            compl = target - num
            if compl in seen: 
                return [seen[compl], i]
            seen[num] = i 

            
