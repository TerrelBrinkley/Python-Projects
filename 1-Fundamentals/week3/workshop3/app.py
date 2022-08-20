from donations_pkg.homepage import show_homepage
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
        username = input("Enter Username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)
    elif (user_option == "2"):
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password
    elif (user_option == "3"):
        print("TODO: Write Donate Functionality")
    elif (user_option == "4"):
        print("TODO: Write Show Donations Functionality")
    elif (user_option == "5"):
        print("Goodbye", authorized_user)
        break
