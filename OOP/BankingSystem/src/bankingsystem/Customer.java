package bankingsystem;
import java.util.Scanner;

public class Customer {
    private final String firstName;
    private final String lastName;
    private final long ID;
    private Account account = null;
    
    public Customer(String fname, String lname, int IDindex) {
        this.firstName = fname;
        this.lastName = lname;
        this.ID = 100001 + IDindex;
    }
    
    public String getFirstName() {
        return this.firstName;
    }
    
    public String getLastName() {
        return this.lastName;
    }
    
    
    public long getID() {
        return this.ID;
    }
    
    public Account getAccount() {
        return this.account;
    }
    
    public void setAccount(double initBal) {
        while (initBal < 5.00f) {
            Scanner sc = new Scanner(System.in);
            System.out.println("Initial balance must be at least $5.00");
            initBal = sc.nextDouble();
        }
        if (this.account == null) {
            this.account = new Account(initBal);
        }
    }
}
