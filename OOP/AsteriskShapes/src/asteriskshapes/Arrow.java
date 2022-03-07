package asteriskshapes;

/**
 *
 * @author Ian Wirawan
 */
public class Arrow {
    
    public void printSelf() {
        for (int i = 0; i < 9; i++) {
            switch (i) {
                case 1  -> System.out.println(" *** ");
                case 2  -> System.out.println("*****");
                default -> System.out.println("  *  ");
            }
        }
    }
}
