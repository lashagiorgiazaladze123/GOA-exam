class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn. Balance: ${self.balance}")
        else:
            print("Insufficient funds!")

    def check_balance(self):
        print(f"Balance: ${self.balance}")

def main():
    account = BankAccount()
    
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        choice = input("Choose option: ")
        
        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Goodbye")
            break
        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()


            


            