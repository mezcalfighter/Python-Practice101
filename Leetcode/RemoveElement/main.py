def removeElement(nums, val):
        nums=nums.sort()
        removed = 0
        i = 0
        while val in nums:
            if nums[i] == val:
                del(nums[i])
                removed += 1
            i+=1
        return removed, nums