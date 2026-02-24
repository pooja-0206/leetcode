#HashSet TC:O(N), SC:O(N)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==len(set(nums)):
            return False
        else:
            return True

#Sorting TC:O(NlogN) SC:O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False
