class customer(bank):
     
    def _init_(self ,username ,balance):
        super().__init__()
        self.balance=balance
        self .username=username

    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
    def withdraw(self, amount):

        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount} has been withdrawn from your account.")
    def get_balance(self):
        return self._balance
