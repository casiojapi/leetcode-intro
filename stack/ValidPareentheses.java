import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack st = new Stack();
        for (int i = 0; i< s.length(); i++) {
            char curr = s.charAt(i);
            if (curr == '(' || curr == '[' || curr == '{') {
                st.push(curr);
            } else if (st.isEmpty()) {
                return false;
            } else {
                char first = (char)st.pop();
                if ((first == '(' && curr != ')') || (first == '[' && curr != ']') || (first == '{' && curr != '}')  )
                    return false;
            }
        }
        return st.isEmpty();
    }

}