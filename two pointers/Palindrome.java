class Solution {
    public boolean isPalindrome(String s) {
        String ss = s.replaceAll("[^0-9a-zA-Z]", "").toLowerCase();
        int len = ss.length();
        for (int i = 0; i < len; i++) {
            if (ss.charAt(i) != ss.charAt(len - 1 - i))
                return false;
        }
        return true;
    }
    
  
}