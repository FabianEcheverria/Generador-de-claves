import string, random
import os

def Main():
    os.system('cls') #Limpia la consola al ajecutar el programa
    print("Welcome to Password Generator")

    def ValidateInput(n):
        try:
            n = int(n)
        except:
            n = ValidateInput(input("Invalid data, try again"))
        return n

    while True:
        upperCase = ValidateInput(input("number of uppercase:"))
        lowerCase = ValidateInput(input("number of lowercase:"))
        numbers = ValidateInput(input("number of numbers:"))

        length = upperCase + lowerCase + numbers
        characters = string.ascii_letters+string.digits+string.punctuation

        password = (" ").join(random.choice(characters) for i in range(length))
        if (sum(c.islower() for c in password) >= lowerCase
            and sum(c.isupper() for c in password) >= upperCase
            and sum(c.isdigit() for c in password) >= numbers):
            break

        print("Your created password is: ", password)

        newPassword = ValidateInput(input("1) Generate new password: \n2) End Software: "))
        if newPassword != 1:
            break
        else:
            continue



Main()
