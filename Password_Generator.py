import ast
import random


def give_me_password(len_password):
    lower_letter = list("abcdefghijklmnopqrstuvwxyz")
    capital_letter = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    number = list("0123456789")

    index_capital_letter = random.randint(1, 4)
    index_number = random.randint(5, 8)
    password = []

    for chars in range(len_password):
        if index_capital_letter == chars:
            password.append(random.choice(capital_letter))
        elif index_number == chars:
            password.append(random.choice(number))
        else:
            password.append(random.choice(lower_letter))
    password = ''.join(password)
    return password


print("PASSWORD GENERATOR")
my_dict = {}
while True:
    print("\n1. Generate a new password for an account.\n2. Get the password for a specified account.\n3. Exit")
    option = input("Please choose an option: ")
    if option == "1":
        account = input("Enter an account: ")
        my_dict[account] = give_me_password(random.randint(9, 16))
        with open('password.txt', 'w') as data:
            data.write(str(my_dict))
        print(f'{account}: {my_dict.get(account)}')

    elif option == "2":
        account = input("Enter the name account: ")
        with open('password.txt') as data:
            info = data.read()
            my_dict = ast.literal_eval(info)
            if my_dict.get(account) is None:
                print("Account no registered, please register it")
            else:
                print(f"{account} : {my_dict.get(account)}")
    elif option == "3":
        print("Exiting...")
        break
    else:
        print("\nPlease choose a valid option.")

