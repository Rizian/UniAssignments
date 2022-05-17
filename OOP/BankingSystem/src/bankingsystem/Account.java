package bankingsystem;

public class Account {
    private double balance;

    public Account(double initBalance) {
        this.balance = initBalance;
    }
    
    public double getBalance() {
        return this.balance;
    }
    
    public boolean withdraw(double amount) {
        if (amount > this.balance) {
            System.out.println("Insufficient balance.");
            return false;
        }
        this.balance -= amount;
        return true;
    }
    
    public boolean deposit(double amount) {
        this.balance += amount;
        return true;
    }
}
