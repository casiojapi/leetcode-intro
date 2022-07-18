import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;



import java.util.Arrays;


class StringComparator implements Comparator{  
    public int compare(Object s1,Object s2){  
        Integer i1 = Integer.valueOf((String)s1);
        Integer i2 = Integer.valueOf((String)s2);
        return Integer.compare(i1, i2);
    }  
}



class Result {
    
   
    /*
     * Complete the 'processLogs' function below.
     *
     * The function is expected to return a STRING_ARRAY.
     * The function accepts following parameters:
     *  1. STRING_ARRAY logs
     *  2. INTEGER threshold
     */

    public static List<String> processLogs(List<String> logs, int threshold) {
    // Write your code here
        
        List<String> res = new ArrayList<String>() {
            public boolean add(String mt) {
                super.add(mt);
                Collections.sort(this, new StringComparator());
                return true;
            } 
        };

        //check if the List is empty, if it is, returns an empty list.
      
            
        HashMap<String, Integer> userTranscationsMap = new HashMap<String, Integer>();
        
        for (String log: logs) {
            String[] current = log.split(" ");
            if (userTranscationsMap.containsKey(current[0])) {
                int transactions = userTranscationsMap.get(current[0]) + 1;
                userTranscationsMap.put(current[0], transactions);
                if (transactions == threshold) {
                    res.add(current[0]);
                }
            } else {
                userTranscationsMap.put(current[0], 1);
                if (1 == threshold) {
                    res.add(current[1]);
                }
            }
            if (current[0] != current[1]) {
                if (userTranscationsMap.containsKey(current[1])) {
                    int transactions = userTranscationsMap.get(current[1]) + 1;
                    userTranscationsMap.put(current[1], transactions);
                    if (transactions == threshold) {
                        res.add(current[1]);
                    }
                } else {
                    userTranscationsMap.put(current[1], 1);
                    if (1 == threshold) {
                        res.add(current[1]);
                    }
                }
            }
        }
        
        return res;
    }

}
