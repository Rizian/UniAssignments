package printarrayinstars;
import java.util.Scanner;
/**
 *
 * @author Ian Wirawan
 */
public class PrintArrayInStars {

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
        
        System.out.println("Result:");
        
        for (int i = 0; i < NUM_ITEMS; i++) {
            String outStr = printStars(items[i]);
            System.out.printf("%d: %s(%d)%n", i+1, outStr, items[i]);
        }
        
    }
    
    public static String printStars(int num) {
        String stars = "";
        for (int i = 0; i < num; i++) {
            stars += "*";
        }
        return stars;
    }
}