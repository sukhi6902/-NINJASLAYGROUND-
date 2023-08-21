import java.util.* ;

import java.io.*; 

/*******************************************

 *

 *   Following is the Pair class structure

 *

 *   class Pair{

 *

 *       char firstLetterOfName;

 *       int avgMarks;

 *

 *       Pair(char firstLetterOfName, int avgMarks){

 *           this.firstLetterOfName = firstLetterOfName;

 *           this.avgMarks = avgMarks;

 *       }

 *   } 

 *

 **********************************************/

 

public class Solution {

    public static Pair averageMarks(char firstLetterOfName, int m1, int m2, int m3) {

        // Write your code here.

        

        int avg=(m1+m2+m3)/3;

        Pair obj = new Pair(firstLetterOfName,avg);

        return obj;

        

 

    }

}

https://www.codingninjas.com/studio/problems/average-marks_9065117?challengeSlug=ninja-slayground&leftPanelTab=0
