def show_homepage():
    print("\n       === DonateMe Homepage ===         ")
    print("-------------------------------------------")
    print("| 1.   Login       | 2.   Register        |")
    print("| 3.   Donate      | 4.   Show Donations  |")
    print("-------------------------------------------")
    print("               5.   Exit                   ")
    print("-------------------------------------------")


def donate(username):
    donation_amt = input("\nEnter amount to donate: ")
    donation_string = username, "donated $", donation_amt
    print("Thank You for your donation!")
    return donation_string
