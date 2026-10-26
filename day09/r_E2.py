def r_E2(nums:list[int], val:int)->int:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast]!= val:
            nums[slow] = nums[fast]
            slow += 1
    return slow

nums = [3,2,2,3,4,5,3,2,4]
val = 3
result = r_E2(nums, val)
print(result)
print(nums[:result])