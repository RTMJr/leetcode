class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in range(len(accounts)):
            curr_wealth = 0
            for j in range(len(accounts[i])):
                curr_wealth += accounts[i][j]
            max_wealth = max(curr_wealth, max_wealth)
            
        return max_wealth
