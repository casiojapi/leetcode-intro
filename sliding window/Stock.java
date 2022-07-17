class Solution {
    public int maxProfit(int[] prices) {
        int minValue = prices[0];
        int maxValue = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < minValue)
                minValue = prices[i];
            else if (prices[i] - minValue > maxValue)
                maxValue = prices[i] - minValue;
        }
        return maxValue;
    }
}