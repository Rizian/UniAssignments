package bankingsystem;
import java.util.Scanner;

public class BankingSystem {

    public static void main(String[] args) {
        final String bankName = "Algobank";
        final Bank Algobank = new Bank(bankName);
        Customer currentUser = null;
        
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Welcome to Algobank\n");
        
        boolean loop = true;
        
        while (loop) {
            System.out.println("What would you like to do?\n");
            System.out.println("1. Register New Account");
            System.out.println("2. Log in");
            System.out.println("3. Deposit (requires login)");
            System.out.println("4. Withdraw (requires login)");
            System.out.println("5. Transfer (requires login)");
            System.out.println("6. Check Balance (requires login)");
            System.out.println("7. Log out");
            System.out.println("8. Quit");

            System.out.print(">> ");
            
            int input = sc.nextInt();

            switch (input) {
                case 1 -> {
                    RegisterAcc(Algobank, sc);
                }
                case 2 -> {
                    currentUser = Login(currentUser, Algobank, sc);
                }
                case 3 -> {
                    if (currentUser != null) {
                        System.out.println("Enter Deposit Amount: ");
                        System.out.print(">> ");
                        
                        double deposit = sc.nextDouble();
                        
                        currentUser.getAccount().deposit(deposit);
                    }
                    else {
                        System.out.println("No Login Detected.");
                        System.out.println("Would you like to log in first? Y/N");
                        System.out.print(">> ");
                        
                        String confirm = sc.next();
                        
                        if (confirm.equalsIgnoreCase("Y") || confirm.equalsIgnoreCase("Yes")) { 
                            currentUser = Login(currentUser, Algobank, sc);
                        }
                    }
                }
                case 4 -> {
                    if (currentUser != null) {
                        System.out.println("Enter Withdrawal Amount: ");
                        System.out.print(">> ");
                        
                        double withdraw = sc.nextDouble();
                        
                        currentUser.getAccount().withdraw(withdraw);
                    }
                    else {
                        System.out.println("No Login Detected.");
                        System.out.println("Would you like to log in first? Y/N");
                        System.out.print(">> ");
                        
                        String confirm = sc.next();
                        
                        if (confirm.equalsIgnoreCase("Y") || confirm.equalsIgnoreCase("Yes")) { 
                            currentUser = Login(currentUser, Algobank, sc);
                        }
                    }
                }
                case 5 -> {
                    if (currentUser != null) {
                        System.out.println("Enter Transfer Target's ID: ");
                        System.out.print(">> ");
                        
                        long targetid = sc.nextLong();
                        
                        System.out.println("Enter Transfer Amount: ");
                        System.out.print(">> ");
                        
                        double amount = sc.nextDouble();
                        
                        if (amount < currentUser.getAccount().getBalance()) {
                            System.out.println("Insufficient funds for transaction.");
                        }
                        
                        for (int i = 0; i < Algobank.getNumCustomers(); i++) {
                            if (Algobank.getCustomer(i).getID() == targetid) {
                                Customer target = Algobank.getCustomer(i);
                                
                                currentUser.getAccount().withdraw(amount);
                                target.getAccount().deposit(amount);
                            }   
                        }
                        System.out.println("Transfer target not found.");
                    }
                    else {
                        System.out.println("No Login Detected.");
                        System.out.println("Would you like to log in first? Y/N");
                        System.out.print(">> ");
                        
                        String confirm = sc.next();
                        
                        if (confirm.equalsIgnoreCase("Y") || confirm.equalsIgnoreCase("Yes")) { 
                            currentUser = Login(currentUser, Algobank, sc);
                        }
                    }
                }
                case 6 -> {
                    if (currentUser != null) {
                        System.out.printf("Your Balance: $%.2f%n", currentUser.getAccount().getBalance());
                    }
                    else {
                        System.out.println("No Login Detected.");
                        System.out.println("Would you like to log in first? Y/N");
                        System.out.print(">> ");
                        
                        String confirm = sc.next();
                        
                        if (confirm.equalsIgnoreCase("Y") || confirm.equalsIgnoreCase("Yes")) { 
                            currentUser = Login(currentUser, Algobank, sc);
                        }
                    }
                }
                case 7 -> {
                    currentUser = null;
                    System.out.println("Logged out Successfully.");
                }
                case 8 -> {
                    loop = false;
                }
                default -> {
                    continue;
                }
            }
        }
        sc.close();
    }
    
    private static void RegisterAcc(Bank bankName, Scanner sc) {
        System.out.println("Enter First Name: ");
        System.out.print(">> ");
        
        String firstname = sc.next();
        
        System.out.println("Enter Last Name: ");
        System.out.print(">> ");
        
        String lastname = sc.next();
        
        bankName.addCustomer(firstname, lastname);
        
        System.out.println("Enter Initial Deposit: ");
        System.out.print(">> ");
        
        double initBal = sc.nextDouble();
        
        Customer newCustomer = bankName.getCustomer(bankName.getNumCustomers()-1);
        newCustomer.setAccount(initBal);
        
        System.out.println("Account Created Successfully.");
        System.out.printf("Your ID: %d%n", newCustomer.getID());
    }
    
    private static Customer Login(Customer currentUser, Bank bankName, Scanner sc) {
        System.out.println("Enter Your ID: ");
        System.out.print(">> ");
        
        long id = sc.nextLong();
        
        for (int i = 0; i < bankName.getNumCustomers(); i++) {
            if (bankName.getCustomer(i).getID() == id) {
                currentUser = bankName.getCustomer(i);
                
                System.out.println("Logged in Successfully.");
                return currentUser;
            }
        }
        if (currentUser == null || currentUser.getID() != id) {
            System.out.println("User Not Found");
            System.out.println("Would you like to register a new account? Y/N");
            System.out.print(">> ");
            
            String confirm = sc.next();
            
            if (confirm.equalsIgnoreCase("Y") || confirm.equalsIgnoreCase("Yes")) {
                RegisterAcc(bankName, sc);
            }
        }
        return currentUser;
    }
}
