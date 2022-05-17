package bankingsystem;
import java.util.ArrayList;

public class Bank {
    private ArrayList<Customer> customers;
    private int numCustomers = 0;
    private final String bankName;
    
    public Bank(String bName) {
        this.bankName = bName;
    }
    
    public void addCustomer(String firstname, String lastname) {
        Customer newCustomer = new Customer(firstname, lastname);
        customers.add(newCustomer);
        numCustomers++;
    }
    
    public int getNumCustomers() {
        return this.numCustomers;
    }
    
    public Customer getCustomer(int index) {
        return customers.get(index);
    }
}
