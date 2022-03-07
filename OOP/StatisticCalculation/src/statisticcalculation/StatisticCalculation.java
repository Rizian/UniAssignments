package statisticcalculation;
import java.util.Scanner;
import java.lang.Math;

/**
 *
 * @author Ian Wirawan
 */
public class StatisticCalculation {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter three numbers: ");
        
        System.out.print("Enter the first number\n>> ");
        float x1 = sc.nextFloat();
        System.out.print("Enter the second number\n>> ");
        float x2 = sc.nextFloat();
        System.out.print("Enter the third number\n>> ");
        float x3 = sc.nextFloat();
        
        double mean;
        double variance;
        double stdDev; // Standard Deviation
        
        // Calculations
        mean = (x1 + x2 + x3) / 3;
        
        double x1var = Math.pow((x1 - mean), 2);
        double x2var = Math.pow((x2 - mean), 2);
        double x3var = Math.pow((x3 - mean), 2);
        variance = (x1var + x2var + x3var) / 3;
        
        stdDev = Math.sqrt(variance);
        
        // Outputs (Rounded to certain decimal places so it isn't too long)
        System.out.printf("Mean = %.3f%n", mean);
        System.out.printf("Variance = %.5f%n", variance);
        System.out.printf("Standard Deviation = %.5f%n", stdDev);
    }
    
}
