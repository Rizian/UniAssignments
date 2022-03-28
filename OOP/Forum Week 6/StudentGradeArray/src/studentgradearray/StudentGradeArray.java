package studentgradearray;
import java.util.Scanner;
import java.util.Arrays;

/**
 *
 * @author Ian Wirawan
 */
public class StudentGradeArray {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter the number of students: ");
        int numStudents = sc.nextInt();
        if (numStudents < 1) {
            System.out.println("THERE HAS TO BE AT LEAST ONE STUDENT");
            return;
        }
        
        int[] items = new int[numStudents];
        for (int i = 0; i < numStudents; i++) {
            System.out.printf("Enter the grade for student %d: ", i+1);
            items[i] = sc.nextInt();
        }
        
        Arrays.sort(items);     // sorts the arrays into ascending numerical
                                // order. Makes getting the min and max easy
                                // by only having to take the first and last
                                // elements of the array.
        double avg = calcAvg(items);
        
        System.out.printf("The average is: %.2f%n", avg);
        System.out.printf("The minimum is: %d%n", items[0]);
        System.out.printf("The maximum is: %d%n", items[numStudents-1]);
    }
    
    public static double calcAvg(int[] arr) {
        double sum = 0;
        for (int i : arr) {
            sum += i;
        }
        sum /= arr.length;
        return sum;
    }
}
