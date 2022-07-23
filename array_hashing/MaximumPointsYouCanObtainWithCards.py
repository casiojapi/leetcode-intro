class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l,r = 0,len(cardPoints) - k
        total=sum(cardPoints[r:])
        maxs=total
        while r < len(cardPoints):
            total = total + cardPoints[l] - cardPoints[r]
            maxs = max(maxs, total)
            r+=1
            l+=1
            
        return maxs
