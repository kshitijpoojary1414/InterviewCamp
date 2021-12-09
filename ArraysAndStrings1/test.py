# from typing import List
class Solution:
    # def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    #     dp = [float('inf')]*n
    #     dp[src] = 0
    #
    #     for i in range(k + 1 ) :
    #         temp = dp[::]
    #         for flight in flights :
    #             source = flight[0]
    #             to = flight[1]
    #             price = flight[2]
    #             if dp[source] != float('inf') and dp[source] + price < temp[to] :
    #                 temp[to] = dp[source] + price
    #         dp = temp[::]
    #
    #     if dp[dst] == float('inf') :
    #         return -1
    #     else :
    #         return dp[dst]
    #
    # def isSubsetSum(arr, n, sum):
    #
    #     # The value of subset[i][j] will
    #     # be true if there is a subset of
    #     # set[0..j-1] with sum equal to i
    #     subset = [[False for x in range(n + 1)]
    #               for y in range(sum + 1)]
    #     count = [[0 for x in range(n + 1)]
    #              for y in range(sum + 1)]
    #
    #     # If sum is 0, then answer is true
    #     for i in range(n + 1):
    #         subset[0][i] = True
    #         count[0][i] = 0
    #
    #     # If sum is not 0 and set is empty,
    #     # then answer is false
    #     for i in range(1, sum + 1):
    #         subset[i][0] = False
    #         count[i][0] = -1
    #
    #     # Fill the subset table in bottom up manner
    #     for i in range(1, sum + 1):
    #         for j in range(1, n + 1):
    #             subset[i][j] = subset[i][j - 1]
    #             count[i][j] = count[i][j - 1]
    #             if (i >= arr[j - 1]):
    #                 subset[i][j] = (subset[i][j] or
    #                                 subset[i - arr[j - 1]][j - 1])
    #
    #                 if (subset[i][j]):
    #                     count[i][j] = (max(count[i][j - 1],
    #                                        count[i - arr[j - 1]][j - 1] + 1))
    #     return count[sum][n]


print(Solution().subsetAnd([16,16]))





