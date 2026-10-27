# 给一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求递增排序。

# 示例 1：

# 输入：nums = [-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 解释：平方后，数组变为 [16,1,0,9,100]
# 排序后，数组变为 [0,1,9,16,100]
# 示例 2：

# 输入：nums = [-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
 

# 提示：

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums 已按 非递减顺序 排序
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n =len(nums)
        result = [0]*n
        left, right = 0, n-1 
        pos = n-1

        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                result[pos] = nums[left]**2
                left+=1
            else:
                result[pos] = nums[right]**2
                right -= 1
            pos -=1

        return result


#理解需要重新过一遍