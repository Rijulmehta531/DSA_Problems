# You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

# Return the maximum area of water that can be trapped between the bars.

# Input: height = [0,2,0,3,1,0,1,3,2,1]

# Output: 9

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        if not height:
            return 0
        res = 0
        l, r = 0, len(height)-1
        maxL, maxR = height[l], height[r]
        while l < r:
            if maxR < maxL:
                r-=1
                maxR = max(height[r], maxR)
                res += maxR - height[r]
            else:
                l+=1
                maxL = max(height[l], maxL)
                res += maxL - height[l]
        return res
if __name__ == "__main__":
    height = [0,2,0,3,1,0,1,3,2,1]
    sol = Solution()
    output = sol.trap(height)
    print(output)