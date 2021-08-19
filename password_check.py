"""A program to check a password"""


PASSWORD_LENGTH = 8


user_password = input("Enter your new password: ")

while len(user_password) < PASSWORD_LENGTH:
    print("Invalid: password must be {} characters long".format(PASSWORD_LENGTH))
    user_password = input("Enter your new password: ")
for i in range(len(user_password)):
    print("*", end='')

