package tempcalculator;
import java.util.Scanner;

/**
 *
 * @author Ian Wirawan
 */
public class TempCalculator {

    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter the Temperature in Celcius (°C)");
        System.out.print(">> ");
        
        float celcius = sc.nextFloat();
        float fahrenheit;
        
        // Calculation
        fahrenheit = (celcius / 5) * 9 + 32;
        
        // Output
        System.out.printf("%.1f degrees Celcius is %.1f degrees Fahrenheit.", celcius, fahrenheit);
       
    }
    
}
