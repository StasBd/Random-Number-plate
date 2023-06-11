letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "1234567890"

import random

def creatnumberplate():
    N1 = random.choice(letters)
    N2 = random.choice(letters)
    #Now going numbers 
    L1 = random.choice(numbers)
    L2 = random.choice(numbers)
    L3 = random.choice(numbers)
    L4 = random.choice(numbers)
    print('Youre new numbers is: ', N1+N2+L1+L2+L3+L4)

creatnumberplate()