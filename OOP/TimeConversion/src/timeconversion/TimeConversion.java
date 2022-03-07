package timeconversion;
import java.util.Scanner;
import java.lang.Math;

/**
 *
 * @author Ian Wirawan
 */
public class TimeConversion {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter the number of seconds\n>> ");
        
        // Separate variables for print format variables
        int inpSeconds = sc.nextInt();
        int seconds = inpSeconds; // makes a separate copy of inpSeconds
        
        // floor divides the seconds to get the corresponding time scale then sets the remaining seconds as itself
        int hours = Math.floorDiv(seconds, 3600);
        seconds %= 3600;
        int minutes = Math.floorDiv(seconds, 60);
        seconds %= 60;
        
        // Output string formatting variables
        String strHours = "hours";
        String strMinutes = "minutes";
        String strSeconds = "seconds";
        
        if (hours == 1) {
            strHours = "hour";
        }
        if (minutes == 1) {
            strMinutes = "minute";
        }
        if (seconds == 1) {
            strSeconds = "second";
        }
        
        // Output
        System.out.printf("%d seconds is equal to %d %s, %d %s, and %d %s.%n", inpSeconds, hours, strHours, minutes, strMinutes, seconds, strSeconds);
    }
}
