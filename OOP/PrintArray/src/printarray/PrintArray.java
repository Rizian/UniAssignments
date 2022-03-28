package printarray;
import java.util.Scanner;
import java.util.Arrays;
/**
 *
 * @author Ian Wirawan
 */
public class PrintArray {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter the number of items: ");
        final int NUM_ITEMS = sc.nextInt();
        if (NUM_ITEMS == 0) {
            System.out.println("THE ARRAY CANNOT BE EMPTY");
            return;
        }
        if (NUM_ITEMS < 0) {
            System.out.println("THE NUMBER OF ITEMS CANNOT BE LESS THAN ZERO");
            return;
        }
        
        int[] items = new int[NUM_ITEMS];
        
        System.out.printf("Enter the %d items (separated by space): ", NUM_ITEMS);
        for (int i = 0; i < NUM_ITEMS; i++) {
            items[i] = sc.nextInt();
        }
        
        System.out.println("Resulting Array: " + Arrays.toString(items));
    }
}
