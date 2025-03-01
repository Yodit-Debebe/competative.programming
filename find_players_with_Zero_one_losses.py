class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = {}

        for winner, loser in matches:
            winners.add(winner)
            if loser in losers:
                losers[loser] += 1
            else:
                losers[loser] = 1
        no_losses = sorted(winners - losers.keys())
        one_loss = sorted([player for player, count in losers.items() if count == 1])
        return [no_losses, one_loss]
