"""Banking account operations including balance display, deposits, withdrawals, and logout."""

def show_balance(balance):
    """Display the current account balance."""
    print("Current balance" + str(balance))


def deposit(balance):
    """Add money to the account balance."""
    amount = input("Enter amount to deposit")
    return balance + float(amount)


def withdraw(balance):
    """Remove money from the account balance."""
    amount = input("Enter amount to withdraw")
    return balance - float(amount)


def logout(name):
    """Display a goodbye message to the user."""
    print("Goodbye " + name + "!")
