#假设有个窗口[左边界，右边界]，变量s代表窗口内所有数的和：
#右边加，把nums[roight]加进s，左边收缩，满足s永远等于窗口内的和
#关键在窗口的收缩
#因为要最短，所以当s大于target的时候，窗口是合法的，记下此时的长度len
#然后试试把左边减掉的s如果s还大，就合法，记下长度len
#所以循环如果s>=target，就记下s，并且左端右移一格，s再减去nums[left]
#如果此时发现s<target,怎么办？就结束了此次循环

#因为nums是正整数这样窗口变长，和一定变大，变短s一定变小

#逻辑理顺就没问题
#外层循环跑什么？
#跑右端右移一位，循环完毕+1
#而左边界呢，则是收缩成立的时候+1
#s做什么，右边+，左边-
#先定义，n=len(nums) left=0数组头开始,,s=0窗口的和
#n是数组长度，range(n)就是把长度从0-n写出来，那放进去right，定义了right
#bast=n+1，此时best是是什么呢，目前找到的最短长度，如果循环结束还是n+1，就可以拿来判断返回0，
#


from typing import List


class Solution:
    def minSubArrayLen(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        s = 0
        best = n + 1
        #外层循环
        for right in range(n):
            s += nums[right]    #做两件事，右边前进一步，然后把新元素加进窗口和
            while s >= target:
                best = min(best,right - left + 1)    #保留住最小的长度值
                s-=nums[left]
                left += 1
        
        return 0 if best == n + 1 else best


#道理明白了，但是代码实现有点绕