def r_E(nums:list[int],val:int)->int:
    size = len(nums)
    i = 0
    while i < size:
        if nums[i] == val:
            for j in range(i+1,size):
                nums[j-1] = nums[j]
            size -= 1
        else:
            i += 1
    return size

nums = [3,2,2,3,4,5,3,2,4]
val = 3
result = r_E(nums, val)
print(result)
print(nums[:result])