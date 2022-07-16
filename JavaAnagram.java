class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;
        
        int[] apariciones = new int[50];

        for (int i = 0; i < s.length(); i++)
            apariciones[s.charAt(i) - 'a']++;
            
        for (int j = 0; j < t.length(); j++)
            apariciones[t.charAt(j) - 'a']--;

        for (int i = 0; i < 50; i++)
            if (apariciones[i] != 0)
                return false;

        return true;
        
    }
}