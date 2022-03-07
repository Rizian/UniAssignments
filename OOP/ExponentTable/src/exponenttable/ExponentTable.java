package exponenttable;
import java.lang.Math;

/**
 *
 * @author Ian Wirawan
 */
public class ExponentTable {

    public static void main(String[] args) {
        int num = 0;
        
        System.out.println("number\tsquare\tcube");
        
        do {
            int square = (int) Math.pow(num, 2);
            int cube = (int) Math.pow(num, 3);
            
            System.out.printf("   %-5s%-8s%s%n", num, square, cube);
            num++;
        }
        while (num <= 10);
    }
}
