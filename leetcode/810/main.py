class Solution:
    def xorGame(self, nums: list[int]) -> bool:
        total = nums[0]
        uniques = set([nums[0]])
        for idx in range(1, len(nums)):
            total ^= nums[idx]
            if nums[idx] not in uniques:
                uniques.add(nums[idx])
            else:
                uniques.remove(nums[idx])
        return total == 0 or ((len(uniques))%2 == 0)