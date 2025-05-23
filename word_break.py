class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_set = set(wordDict)  # Convert list to set for O(1) lookups
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string can be segmented
        
        for i in range(1, n + 1):
            for j in range(i):
                # Check if s[j:i] is in the dictionary and dp[j] is True
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  
        return dp[n]
