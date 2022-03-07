package asteriskshapes;
import java.util.Scanner;

/**
 *
 * @author Ian Wirawan
 */
public class AsteriskShapes {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // Sets the scanner to detect keyboard inputs
        
        System.out.println("Enter a number to print:\n\t1. Box\n\t2. Oval\n\t3. Arrow\n\t4. Diamond"); // Prints out the available options
        System.out.print(">> ");
        
        int inputNum = sc.nextInt(); // Reads and saves an integer input
        
        System.out.println(); // Empty line for spacing
        
        switch (inputNum) {
            // Switch statement for each case.
            // Builds a new object specified by the selection and runs the custom print method
            case 1 -> {
                asteriskshapes.Box obj = new asteriskshapes.Box();
                obj.printSelf();
            }
            case 2 -> {
                asteriskshapes.Oval obj = new asteriskshapes.Oval();
                obj.printSelf();
            }
            case 3 -> {
                asteriskshapes.Arrow obj = new asteriskshapes.Arrow();
                obj.printSelf();
            }
            case 4 -> {
                asteriskshapes.Diamond obj = new asteriskshapes.Diamond();
                obj.printSelf();
            }
            default -> System.out.println("Invalid Selection");
        }
        
    }
    
}
