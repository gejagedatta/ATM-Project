class ATM:
    def __init__(self):
        self.balance = 0  

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}₹ . Current balance is {self.balance}₹ "

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew {amount}₹ . Current balance is {self.balance}₹ "
        else:
            return "Sorry, insufficient funds. Withdrawal not processed."


def run_atm():
    atm = ATM()
    
    while True:
        print("\n ATM Simulator ")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            print(f"Your balance is: {atm.check_balance()}₹ ")
        elif choice == '2':
            amount = float(input("Enter deposit amount: ₹ "))
            print(atm.deposit(amount))
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: ₹ "))
            print(atm.withdraw(amount))
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1-4.")

if __name__ == "__main__":
    run_atm()
