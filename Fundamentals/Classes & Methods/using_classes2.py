class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)


user1 = User("jane", "jane@nucamp.co", "janespassword")
print("Your current password is:", user1.password)

updatedPassword = input("Please enter a new password: ")

user1.change_password(updatedPassword)
