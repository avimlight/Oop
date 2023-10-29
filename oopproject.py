from bankaccount import *

Dave = BankAccount(100, "dave")
Gray = BankAccount(200, "gray")
Dave.getBalance()
Gray.getBalance()
Gray.deposit(2000)

Gray.transfer(1000, Dave)
# Gray.withdraw(200)
# Gray.withdraw(4000)
Jim = InterestRewardsAccount(1000, "jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Dave)
Blaze = SavingsAcct(1000, "Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(1000, Gray)
Blaze.deposit(2000)

Blaze.withdraw(200)
