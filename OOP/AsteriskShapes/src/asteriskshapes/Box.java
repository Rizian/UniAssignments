package asteriskshapes;

/**
 *
 * @author Ian Wirawan
 */
public class Box {
    
    public void printSelf() {
        for (int i = 0; i < 9; i++) {
            if (i == 0 || i == 8) {
                System.out.println("*********");
            }
            else {
                System.out.println("*       *");
            }
        }
    }
}
