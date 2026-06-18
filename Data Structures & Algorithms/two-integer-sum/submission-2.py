class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #for i in range(len(nums)):
            #for j in range(len(nums)):
                #if ((nums[i] + nums[j]) == target) and (i!=j) :
                    #return sorted([i,j]) 

        map_dict = {}
        for i,n in enumerate(nums):
            complement = target - n
            if complement in map_dict:
                return [map_dict[complement], i]
            map_dict[n] = i
