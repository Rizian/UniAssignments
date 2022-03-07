package quadraticsolver;
import java.util.Scanner;
import java.lang.Math;

/**
 *
 * @author Ian Wirawan
 */
public class QuadraticSolver {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter a quadratic (2nd degree polynomial (ax^2 + bx + c = 0)) equation you would like to solve:");
        
        System.out.print("Enter the coefficient a: ");
        double var1 = sc.nextInt();
        System.out.print("Enter the coefficient b: ");
        double var2 = sc.nextInt();
        System.out.print("Enter c: ");
        double var3 = sc.nextInt();
        
        double result; // Variable to store result
        
        
        if (var1 == 0) {
            result = var3 / var2;
        }
        else {
            result = solveQuadratic(var1, var2, var3);
        }
        
        // Output
        if (result == 0.0) {
            System.out.println("No solution found");
        }
        else {
            System.out.printf("x = %.2f%n", result);
        }
    }
    
    public static double solveQuadratic(double i, double j, double k) {
        double posResult;
        double negResult;
        posResult = (-j + Math.sqrt(Math.pow(j, 2)- 4 * i * k)) / (2 * i);
        negResult = (-j - Math.sqrt(Math.pow(j, 2)- 4 * i * k)) / (2 * i);
        if (i * Math.pow(posResult, 2) + j * posResult + k == 0) {
            return posResult;
        }
        if (i * Math.pow(negResult, 2) + j * negResult + k == 0) {
            return negResult;
        }
        return 0.0;
    }
}
