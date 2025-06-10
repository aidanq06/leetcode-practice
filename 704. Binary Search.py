class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left = start of list
        # right = end of the list
        # THESE ARE ALL INDICES
        left = 0
        right = len(nums)-1

        while left <= right:
            # // = floor division
            middle = (left+right) // 2

            if nums[middle] == target:
                return middle
            # if the target is bigger than the left side, i want to start at the old middle + 1
            elif target>nums[middle]:
                left=middle+1
            # if the target is smaller than the right side, i want to end at the old middle -1
            elif target<nums[middle]:
                right=middle-1
        return -1
