def login(database, username, password):
    if username in database:
        if password == database[username]:
            print("Welcome", username)
            return username
        print("Incorrect Password")
        return ""
    print("Username not found")
    return ""


def register(database, username):
    if username in database.keys():
        print("Username already exits")
        return ""
    print("Username has been registered")
    return username
