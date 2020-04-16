import random

code = [str(i) for i in random.sample(range(10), 3)]
print(code)

print("Welcome Code Breaker! Let's see if you can guess my 3 digit number")
print("Code has been generate, please guess a 3 digit number")

while True:
    user_guess = list(input("What is your guess?"))

    if user_guess == code:
        print("You break the code....!!!!")
        break

    clues = []
    
    for index, num in enumerate(user_guess):
        if num == code[index]:
            clues.append('Match')
        elif num in code:
            clues.append('Close')

    if not clues:
        clues = ['Nope']

    print(clues)

