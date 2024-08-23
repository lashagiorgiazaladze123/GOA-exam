class BankAccount:
    def __init__(My):
        My.balance = 0
    def deposite(My, amount):
        My.balance += amount
        print(f"${amount}deposite. balance: ${My.balance}")
    def withdraw(My, amount):
        if amount <= My.balance:
            My.balance -= amount 
            print(f"${amount}withdraw balance${My.balance}")
        else:
            print("insufficent funds!")
        
        def check_balance(My):
            print(f"balance ${My.balance}")

        def main():
            account = BankAccount()
            while True:
                print("\n1. deposite\n2. withdrow\n3. My.balance\n4. exit")
            choice = (input("choose option"))
            if choice == '1':
                float(input("enter amount to deposite"))
                account.deposite (amount)
            elif choice == '2':
                amount =  float(input('amount to withdraw:'))
                account.withdraw(amount)
            elif choice == '3':
                amount = float(input('your balance'))
                amount = My.balance(amount)
            elif choice == '4':
                print("goodbye")
            else: 
                print("wrong choice")
            
            if __name__ == "__main__":
                main()
                

            


            