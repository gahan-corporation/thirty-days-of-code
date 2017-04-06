import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class DayOne {

  public static void main(String[] args) {
    int i = 4;
    double d = 4.0;
    String s = "Run's house ";

    Scanner scan = new Scanner(System.in);

    int j = scan.nextInt();

    double e = scan.nextDouble();
    scan.nextLine(); // To consume the remaining newline.
    String t = scan.nextLine();

    int k = i + j;
    System.out.println(k);

    double f = d + e;
    System.out.println(f);

    String u = s + "" + t;

    scan.close();

  }

}
