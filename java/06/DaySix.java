import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class DaySix {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String[] s = new String[n];

        in.nextLine();
        for (int i = 0; i < n; i++) {
          String e = new String();
          String o = new String();
          s[i] = in.nextLine(); 

          for (int j = 0; j < s[i].length(); j++) {
            char c = s[i].charAt(j);
            if (j % 2 == 1) {
              o = o + c;
            } else {
              e = e + c;
            }
          }
          System.out.println(e + " " + o);
        }
    }
}
