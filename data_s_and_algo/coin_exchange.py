class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp= [amount+1]* (amount+1) # collecting every value in dp. we will go from 0 to the amount, so to the max value each element will be going is 8; initialization value of amount + 1 is typically chosen to be a value that represents "infinity"
        dp[0]=0 #base case, if we want the value of 0 then it will take 0 coins, we start at 0

        for a in range(1, amount+1): # we are going from 1 all the way to the amount, which is 7
            for coin in coins: #we are going thru every coin available,(1,3,4,5), we will compute the a amount
                if a - coin >=0: # we are computing a amount, if it's greater than 0 then we will continue searching. this is called the recurance relation
                    dp[a] = min(dp[a], 1+dp[a-coin]) #the 1 comes from the current coin we are using, first inner loop with a =1, coin =1.it will not do second,third,andfourth inner loop when the coin is  3, 4, and 5. 1-3 not greater than 0, 1-4 not greater than 0...
                                                                    #it will now do the outer loop with a = 2, and inner loop will start with coin 1 again
                                                                   #ex1:  #when  loops runs with   ex2: # when loop runs with
        return dp[amount] if dp[amount] != amount + 1 else -1               # a = 1  coin = 1               # a = 2    coin = 1
                                                                            # dp[1] = 1 + dp[1-1]            # dp[2] = 1 + dp[2-1]
                                                                            # dp[1] = 1                      # dp[1] = 1 +1
                                                                                                            # dp[1] = 2
solution = Solution()                                                                               #in dp[a] = min(dp[a], 1+dp[a-coin])
coins = [1,3,4,5]                                                                                   #   dp[2] = min(dp[2], 1 + dp[2-1])   "will give us dp[1] which is equel to 1 in the current form of the array" [0, 1, 8, 8, 8, 8, 8, 8] remember that the array will keep changing
amount = 7                                                                                         #    dp[2] = min(1, 2)  .. it gets 2 since it is the minimum
result = solution.coinChange(coins,amount)                                                         #now the list looks like this: dp = [0, 1, 2, 8, 8, 8, 8, 8]
print(result)

                                                                         # Note: when a=1 and coin = 3 will not pass the if statement since 1-3 = -2
# ex: from coins = [1,3,4,5] amount = 7                                  #with  a=1 coin=4 will not pass either 1-4 = -3. same with a=1 coin = 5 1-5 = -4
# it goes from 0 to the amount, in this case 7                           #so far it looks like this dp = [0, 1, 2, 8, 8, 8, 8, 8]
# we want the value  = #of coins needed                                  #when a=3 and coin=1 since 3-1=2, it will have min(8, 1+ dp[3-1]) which is min(8, 1+ dp[2]).
#dp[0] = 0                                                               #.. it will then have min(8, 1+2), after dp = [0, 1, 2, 3, 8, 8, 8, 8] (keeps track of the #of coins)
#dp[1] = 1                                                               #when a=3 and coin=3 then dp[3] = min(dp[3],1+dp[3-3])>> dp[3]=min(3,1+dp[0])>> dp[3]=1..
#dp[2] = 2                                                               #..the list looks like dp =[0, 1, 2, 1, 8, 8, 8, 8]
#dp[3] = 1                                                               #at the end db = [0, 1, 2, 1, 1, 1, 2, 2], which keep track of the minimum amount coins needed to reach a certain value(amount) with the coins that are provided
#dp[4] = 1                                                               #to reach 0 we need 0 coins, reach 1 needs 1 coin, reach amount of 2 we need 2 coins of 1, etc..
#dp[5] = 1                                                               #at the end dp[7] = 2 coins, one 4 coin and one 3 coin, or one 3 coin and one 4 coin.
#dp[6] = 2                                                               #lastly in line 36 we return dp[amount] if it is not the default value(8)
 #       coins+coints to complete the missing value                      #  2 != 7+1    ..so it will return 2
#dp[7] =  1 + dp[6]          #using coin=1
#       = 1 + 2
#       = 3 coins           .. not minimal solution so we now go to coin 3

#dp[7] =  1 + dp[4]          #using coin =3
#       = 2 coins             #best solution minimum number of coins

#dp[7] =  1 + dp[3]          #using coin =4
#       = 2 coins              #best solution minimum number of coins

#dp[7] =  1 + dp[2]          #using coin =5
#       = 1 + 2
#       = 3 coins

# coin = 4
# a = 7
# dp[7] = 1 + dp[7-4]


#to review solution with visual explanation: https://www.youtube.com/watch?v=H9bfqozjoqs
