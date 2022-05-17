package bankingsystem;
import java.util.Scanner;

public class BankingSystem {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final String bankName = "Algobank";
        final Bank Algobank = new Bank(bankName);
        Customer currentUser = null;
        
        System.out.println("Welcome to Algobank\n\n");
        
        while (true) {
            System.out.println("What would you like to do?\n");
            System.out.println("1. Register New Account");
            System.out.println("2. Log in");
            System.out.println("3. Deposit (requires login)");
            System.out.println("4. Withdraw (requires login)");
            System.out.println("5. Transfer (requires login)");
            System.out.println("5. Log out");
            System.out.println("6. Quit");

            System.out.print(">> ");
            int input = sc.nextInt();

            switch (input) {
                case 1 -> {
                    RegisterAcc(Algobank, sc);
                }
                case 2 -> {
                    System.out.println("Enter Your ID: \n");
                    System.out.print(">> ");
                    long id = sc.nextLong();
                    for (int i = 0; i < Algobank.getNumCustomers(); i++) {
                        if (Algobank.getCustomer(i).getID() == id) {
                            currentUser = Algobank.getCustomer(i);
                            break;
                        }
                    }
                    if (currentUser == null) {
                        System.out.println("User Not Found");
                        System.out.println("Would you like to register a new account? Y/N");
                        String confirm = sc.nextLine();
                        if (confirm.equalsIgnoreCase("Y") || confirm.equalsIgnoreCase("Yes")) {
                            RegisterAcc(Algobank, sc);
                        }
                    }
                }
                case 3 ->
            }
        }
        
        sc.close();
    }
    
    private static void RegisterAcc(Bank bankName, Scanner sc) {
        System.out.println("Enter First Name: ");
                    System.out.print(">> ");
                    String firstname = sc.nextLine();
                    System.out.println("Enter Last Name: ");
                    System.out.print(">> ");
                    String lastname = sc.nextLine();
                    bankName.addCustomer(firstname, lastname);
                    System.out.println("Enter the starting deposit: ");
                    System.out.print(">> ");
                    Customer newCustomer = bankName.getCustomer(bankName.getNumCustomers());
                    double initBal = sc.nextDouble();
                    newCustomer.setAccount(initBal);
                    System.out.println("Account has been created.");
                    System.out.printf("Your ID: %d", newCustomer.getID());
    }
}
