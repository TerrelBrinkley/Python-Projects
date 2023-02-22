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
    print(f'{username} donated ${donation_amt}\nThank you for your donation!\n')
    donation_string = username + " donated $" + donation_amt
    return donation_string


def show_donations(donations):
    print("\n--- All Donations ---")
    if donations:
        print(donations)
    else:
        print("Currently, there are no donations.")
