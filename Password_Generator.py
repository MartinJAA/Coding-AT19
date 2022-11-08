# password = chars > 8 and chars <= 16
#           at least one capital letter
#           at least one number
#           at least one lower letter
import random

#Another try
lower_letter = "abcdefghijklmnopqrstuvwxyz"
capital_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"

len_password = random.randint(9, 16)            #chars
index_capital_letter = random.randint(1,4)
index_number = random.randint(5,8)

for chars in range(len_password):
    if index_capital_letter == chars:
        print(random.choice(capital_letter), end='')
    elif index_number == chars:
        print(random.choice(number), end='')
    else:
        print(random.choice(lower_letter), end='')

