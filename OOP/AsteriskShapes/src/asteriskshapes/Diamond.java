package asteriskshapes;

/**
 *
 * @author Ian Wirawan
 */
public class Diamond {
    
    public void printSelf() {
        for (int i = 0; i < 9; i++) {
            switch (i) {
                case 0, 8 -> System.out.println("    *    ");
                case 1, 7 -> System.out.println("   * *   ");
                case 2, 6 -> System.out.println("  *   *  ");
                case 3, 5 -> System.out.println(" *     * ");
                case 4    -> System.out.println("*       *");
            }
        }
    }
}
