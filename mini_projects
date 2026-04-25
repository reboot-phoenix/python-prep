import random

number = random.randint(1,50)

print("Guess the number between (1-50): ")
print("You have 3 chances!")

for i in range(3):
  guess = int(input("Enter your guess: "))

  if (guess == number):
    print("You Win!")
    break
  elif (guess < number):
    print("Your guess is too low!")
  else:
    print("Your guess is too high!")
else:
    print("You Lost!")
    print("The number was: ", number)
