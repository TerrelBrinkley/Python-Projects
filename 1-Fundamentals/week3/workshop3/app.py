from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {
    "admin": "password123",
    "terrel": "pass123"
}
donations = []
authorized_user = ""


while True:
    show_homepage()

    if authorized_user == "":
        print("You must be logged in to donate")
    else:
        print("Logged in as:", authorized_user)

    user_option = input("Choose an option: ")

    if (user_option == "1"):
        username = input("\nEnter Username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)
    elif (user_option == "2"):
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password
    elif (user_option == "3"):
        if authorized_user == "":
            print("\nYou are not logged in.")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
    elif (user_option == "4"):
        show_donations(donations)
    elif (user_option == "5"):
        print("Goodbye", authorized_user)
        break
