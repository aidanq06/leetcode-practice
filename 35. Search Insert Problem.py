class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1

        # check endpoints
        if target>nums[-1]:
            return len(nums)
        elif target<nums[0]:
            return 0

        while left<=right:
            #binary search
            middle=(right+left)//2
            if nums[middle] == target:
                return middle
            if nums[middle]>target:
                right=middle-1
            elif nums[middle]<target:
                left=middle+1
        # returning left at the end, since at some point right is going to be greater than left, canceling out the while loop
        # this causes the left value to be the correct answer, based on backtesting
        return left
