import random



def LoginId8():

    lowerchars = ['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upperchars = ['A', 'B', 'C', 'D', 'E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    specialchars = ['&', '!', '*', '@', '#', '^', '$', '%']

    numericchars = ['1', '2', '3', '4', '5','6','7','8','9','0']

    password = random.choice(lowerchars) + random.choice(upperchars) + random.choice(numericchars) + random.choice(specialchars)

    password = password + random.choice(lowerchars) + random.choice(upperchars) + random.choice(numericchars) + random.choice(specialchars)

    return password
    
def LoginId16():

    lowerchars = ['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upperchars = ['A', 'B', 'C', 'D', 'E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    specialchars = ['&', '!', '*', '@', '#', '^', '$', '%']

    numericchars = ['1', '2', '3', '4', '5','6','7','8','9','0']

    password = random.choice(lowerchars) + random.choice(upperchars) + random.choice(numericchars) + random.choice(specialchars)

    password1 = password + random.choice(lowerchars) + random.choice(upperchars) + random.choice(numericchars) + random.choice(specialchars)
    
    password2 = password1 + random.choice(lowerchars) + random.choice(upperchars) + random.choice(numericchars) + random.choice(specialchars)
    
    password3 = password2 + random.choice(lowerchars) + random.choice(upperchars) + random.choice(numericchars) + random.choice(specialchars)
    
    return password3

def ATMpin4():

    numericchars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in range(0, 4):
        password = random.choice(numericchars) + random.choice(numericchars) + random.choice(numericchars) + random.choice(numericchars)
        return password 
        
def ATMpin6():

    numericchars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in range(0, 6):
        password = random.choice(numericchars) + random.choice(numericchars) + random.choice(numericchars) + random.choice(numericchars) + random.choice(numericchars) + random.choice(numericchars)
        return password 

print("Choice:\n 1 - Password for Social Accounts(8-character)\n 2 - Password for Social Accounts(16-character)\n 3 - Password for ATM Card(4-digit)\n 4 - Password for ATM Card(6-digit)\n")
a = input("Please enter your choice:\n")

a = int(a)

if a is 1:
    print("8-character assword is: " + LoginId8())
elif a is 2:
    print("16-character password is: " + LoginId16()) 
elif a is 3:
    print("Your 4-digit ATM pin is: " + ATMpin4())
elif a is 4:
    print("Your 6-digit ATM pin is: " + ATMpin6())
else:
    print('Wrong Choice')
    