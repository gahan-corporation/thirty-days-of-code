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

        for (int i = 0; i < n; i++) {
          s[i] = in.nextLine(); 
          System.out.println(s[i]);
        }
    }
}
