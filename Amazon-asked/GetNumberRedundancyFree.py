# Problem: 
# Your team at AMZ is developing a new algorithm for suggesting passwords when a user sets up a NEW account
# A string of lowercase English characters is said to be redundancy-free if each character occurs at most once in the string.
# In order to ensure minimum redundancy, the developers suggest a password that has the
# minimum number of redundancy-free segments it can be divided into.
# Given a string, password, find the minimum number of redundancy-free segments we can divide it into.

# Function Description
# Complete the function getNumberRedundancyFree in the editor.

# getNumberRedundancyFree has the following parameter:
# string password: the given password
# Returns --> int: the number of segments we can divide the string into

# Exanples:
# Input:  password = "alabama"
# Output: 4
# Explanation: The minimum partitions are "al", "ab", "a", "ma".


class Solution:
  def getNumberRedundancyFree(self, password: str) -> int:
    charSet = set()
    res = 1

    for i in range(len(password)):
      if password[i] in charSet:
        res+=1
        charSet.clear()
      charSet.add(password[i])
    return res
    
#For testing
if __name__ == "__main__":
    password = "aabcdea"
    sol = Solution()
    output = sol.getNumberRedundancyFree(password)
    print(output)