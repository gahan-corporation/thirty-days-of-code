import java.util.*;
import java.math.*;

public class DayTwo {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double mealCost = scan.nextDouble(); // original meal price
        int tipPercent = scan.nextInt(); // tip percentage
        int taxPercent = scan.nextInt(); // tax percentage
        scan.close();
        float totalCost;
      
        // Write your calculation code here.
        float tip = (float)mealCost * tipPercent/100;
        float tax = (float)mealCost * taxPercent/100;
      
        totalCost = (float)mealCost + tip + tax;
        // cast the result of the rounding operation to an int and save it as totalCost 
        int total = (int) Math.round(totalCost);
      
        // Print your result
        System.out.println("The total meal cost is "+total+" dollars.");
    }
}
