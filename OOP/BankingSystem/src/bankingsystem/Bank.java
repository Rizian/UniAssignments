package bankingsystem;
import java.util.ArrayList;

public class Bank {
    private ArrayList<Customer> customers = new ArrayList<>(100);
    private int numCustomers = 0;
    private final String bankName;
    private int IDindex = 0;
    
    public Bank(String bName) {
        this.bankName = bName;
    }
    
    public void addCustomer(String firstname, String lastname) {
        Customer newCustomer = new Customer(firstname, lastname, IDindex);
        customers.add(newCustomer);
        numCustomers++;
        IDindex++;
    }
    
    public int getNumCustomers() {
        return this.numCustomers;
    }
    
    public Customer getCustomer(int i) {
        return customers.get(i);
    }
}
