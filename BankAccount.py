class BankAccount:
    def __init__(self, account_number, customer_name, balance, date_of_opening):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = date_of_opening

    def deposit(self, amount):
        self.balance += amount
        return f"Amount Deposited: {amount}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Amount Withdrawn: {amount}"
        else:
            return "Insufficient balance"

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")


account_number = int(input("Enter account number: "))
customer_name = input("Enter customer name: ")
balance = float(input("Enter initial balance: "))
date_of_opening = input("Enter date of account opening (YYYY-MM-DD): ")


Myaccount = BankAccount(account_number, customer_name, balance, date_of_opening)


print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Customer Details")
choice = int(input("Select an option: "))

if choice == 1:
    amount = float(input("Enter amount to deposit: "))
    print(Myaccount.deposit(amount))
elif choice == 2:
    amount = float(input("Enter amount to withdraw: "))
    print(Myaccount.withdraw(amount))
elif choice == 3:
    Myaccount.check_balance()
elif choice == 4:
    Myaccount.customer_details()
else:
    print("Invalid option.")