# You are given an integer array heights where heights[i] represents the height of the ith bar.

# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

# Example 1:
# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36



from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l,r = 0, len(heights)-1

        while l<r:
            area = (r-l) * min(heights[l], heights[r])
            res = max(area, res)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return res
if __name__ == "__main__":
    heights = [1,7,2,5,4,7,3,6]
    sol = Solution()
    output = sol.maxArea(heights)
    print(output)