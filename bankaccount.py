class BankAccount:

    allBankAccounts = []
    
    def __init__ (self, interestRate, balance):
        self.interestRate = interestRate
        self.balance =  balance
        BankAccount.allBankAccounts.append(self)
    

    def deposit (self, amount):
        self.balance += amount
        return self

    def make_withdrawal (self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}.")

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.interestRate
        return self


    def printInformation(self):
        print(f"Account interest: {self.interestRate}. Account balance: {self.balance}.")


    @classmethod
    def printAllAccountsInfo(cls):
        print(f"This is the information for all the accounts")
        for account in cls.allBankAccounts:
            account.printInformation()