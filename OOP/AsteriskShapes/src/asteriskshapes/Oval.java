package asteriskshapes;

/**
 *
 * @author Ian Wirawan
 */
public class Oval {
    
    public void printSelf() {
        for (int i = 0; i < 9; i++) {
            switch (i) {
                case 0, 8 -> System.out.println("   ***   ");
                case 1, 7 -> System.out.println(" *     * ");
                default   -> System.out.println("*       *");
            }
        }
    }
}
