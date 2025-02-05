# The data analysts of Amazon are working on a prototype service to prune the data. The service takes in an array data of n integers and an integer max_distinct. It removes some elements from the array until the final array contains at most max_distinct distinct elements.

# Given data and max_distinct, find the minimum number of elements the service must remove such that the resulting array contains at most max_distinct distinct elements.

# Function Description

# Complete the function getMinRemovals in the editor.

# getMinRemovals takes the following arguments:

# int data[n]: The data passed to the service
# int max_distinct: The maximum number of distinct elements in the final array
# Returns

# int: The minimum number of elements to be removed from the array

# Example 1:

# Input:  data = [1, 2, 3, 2, 1], max_distinct = 2
# Output: 1 
# Explanation: It is optimal to remove a single element, 3, from the array to leave [1, 2, 2, 1] that contains only 2 distinct elements. Hence the answer is 1.

from typing import List

class Solution:
  def getMinRemovals(self, data: List[int], max_distinct: int) -> int:
    count = {}
    res = 0
    arr = [[] for i in range(len(data)+1)]
    for d in data:
      count[d] = count.get(d,0) + 1
    if len(count) == max_distinct:
      return 0

    for key, value in count.items():
      arr[value].append(key)

    l = 1
    while len(count) > max_distinct and l < len(arr):
      for n in arr[l]:
        if len(count) > max_distinct:
          del count[n]
          res+=l
      l+=1
    return res

    
if __name__ == "__main__":
    data = [1,2,3,2,1]
    sol = Solution()
    output = sol.getMinRemovals(data,2)
    print(output)