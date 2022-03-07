package valueswitcher;

/**
 *
 * @author Ian Wirawan
 */
public class ValueSwitcher {

    public static void main(String[] args) {
        //Variables
        int x = 5;
        int y = 10;
        int temp; // Temporary variable to store intermediary value
        
        temp = y;
        y = x;
        x = temp;
        
        // Output
        System.out.printf("x = %d, y = %d%n", x, y); // Expected result: "x = 10, y = 5") 
    }
}
