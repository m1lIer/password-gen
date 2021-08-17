import time
import random

value = int(input("Password length: "))
print("\n\nPossible symbols: \n1. only letters and numbers \n2. other symbols \n")
types = int(input())
symbols = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '0',11: 'a', 12: 'b', 13: 'c',
14: 'd', 15: 'e', 16: 'f', 17: 'g', 18: 'h', 19: 'i', 20: 'j', 21: 'k', 22: 'n', 23: 'o', 24: 'p', 25: 'r', 26: 'x', 27: 'y', 28: 'z', 29: '[', 30: ']', 31: '{', 32: '}', 33: '*', 34: '=', 35: ')'}
y_n = input("\nDo you want to enter key words? [Y / n] ")
y_n = y_n.lower()
if y_n == "n":
    keyword = ""
if y_n == "y":
    print("\n\n\033[31m!WARNING!\nkeyword must be less than Password length\033[0m\n\n")
    keyword = input("Write key word: ")
    if len(keyword) > value:
        print("\033[31mError\033[0m")
        exit()
password = '';
run = True
if types == 1:
    while(run):
        keyword_len = len(keyword)
        len = value - keyword_len
        rand1part = random.randint(1, len)
        for i in range(rand1part):
            rand = random.randint(1,28)
            password += symbols[rand]
        password += keyword
        part3 = value - rand1part - keyword_len
        for i in range(part3):
            rand = random.randint(1,28)
            password += symbols[rand]

        run = False
    print("\n" + password)
if types == 2:
    while(run):
        keyword_len = len(keyword)
        len = value - keyword_len
        rand1part = random.randint(1, len)
        for i in range(rand1part):
            rand = random.randint(1,35)
            password += symbols[rand]
        password += keyword
        part3 = value - rand1part - keyword_len
        for i in range(part3):
            rand = random.randint(1,35)
            password += symbols[rand]

        run = False
    print("\n" + password)
if types != 1 and types != 2:
    print("\033[31mError\033[0m")
