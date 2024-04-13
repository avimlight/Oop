# Python Banking System

Welcome to the Python Banking System project! This codebase implements a simple banking system simulation using object-oriented programming in Python. The system includes basic functionalities such as account creation, deposits, withdrawals, and transfers, along with specialized features for handling exceptions and rewarding accounts with interest on deposits.

## Features

- **BankAccount**: Basic bank account operations including account creation, balance inquiries, deposits, and withdrawals.
- **InterestRewardsAccount**: Inherits from `BankAccount`, adding a 5% interest reward to each deposit.
- **SavingsAcct**: A type of `InterestRewardsAccount` that includes transaction fees for withdrawals.
- **BalanceException**: A custom exception class to handle scenarios where a transaction exceeds the account balance.

## Modules and Classes

- **BankAccount**: Main class for creating bank accounts and handling deposits and withdrawals.
- **InterestRewardsAccount**: Subclass of `BankAccount` that enhances the deposit method to include interest.
- **SavingsAcct**: Further specialization of `InterestRewardsAccount`, applying a withdrawal fee.
- **BalanceException**: Custom exception class for managing balance-related errors in transactions.
