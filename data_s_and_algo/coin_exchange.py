#failed multile test cases
# def coinChange(coins: list[int], amount: int) -> int:
#     coins[:] = sorted(coins)
#     coins[:] = coins[::-1]
#     print(coins)
#     total = 0
#     coin_num = 0
#     # print(coins)
#     print(1//2)
#     for coin in coins:
#         if amount>=0:
#             coin_num= amount//coin #will get 2 total =2, then will get 0 coin; total =2 ;
#             total+=coin_num #total will be 2, then 2 again, then 3
#             amount -= coin_num *coin  # it will be 1 , then 1 again,
#             if amount == 0:
#                 return total
#     return -1


# coins = [186,419,83,408]
# amount = 6249
# result = coinChange(coins,amount)
# print(result)

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp= [amount+1]* (amount+1) # collecting every value in dp. we will go from 0 to the amount, so to the max value each element will be going is 12 (Exclusive, so 11)
        dp[0]=0 #base case, if we want the value of 0 then it will take 0 coins, we start at 0

        for a in range(1, amount+1): # we are going from 1 all the way to the amount 11
            for coin in coins: #we are going thru every coin available, we will compute the a amount
                if a - coin >=0: # we are computing a amount
                    dp[a] = min(dp[a], 1+dp[a-coin]) #the 1 comes from the current coin we are using
        print(amount + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1


solution = Solution()
coins = [1,3,4,5]
amount = 7
result = solution.coinChange(coins,amount)
print(result)


# ex: from coins = [1,3,4,5] amount = 7
# it goes from 0 to the amount, in this case 7
# we want the value  = #of coins needed
#dp[0] = 0
#dp[1] = 1
#dp[2] = 2
#dp[3] = 1
#dp[4] = 1
#dp[5] = 1
#dp[6] = 2
 #       coins+coints to complete the missing value
#dp[7] =  1 + dp[6]          #using coin 1
#       = 1 + 2
#       = 3 coins           .. not minimal solution so we now go to coin 3

#dp[7] =  1 + dp[4]          #using coin 3
#       = 2 coins             #best solution minimum number of coins

#dp[7] =  1 + dp[3]          #using coin 4
#       = 2 coins              #best solution minimum number of coins

#dp[7] =  1 + dp[2]          #using coin 5
#       = 1 + 2
#       = 3 coins

# coin = 4
# a = 7
# dp[7] = 1 + dp[7-4]
