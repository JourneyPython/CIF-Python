import random
number = random.randint(1, 100)

attempts = 0
max_attempts = 3
print("<<<<WELCOME TO THE GUESSING GAME>>>>")
print("I'm thinking of a number between 1 and 100. You have 3 attempts to guess the number.")

while attempts < max_attempts:
    try:
        guess = int(input("Your guess (integer between 1 and 100):"))
        if not (1 <= guess <= 100):
                print("Please guess a number within the range of 1 to 100.")
                continue

        attempts += 1
        
        if guess == number:
            print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
        
        elif attempts == 3: 
            exit
        
        elif guess < number:
            print("Too low! Try a higher number.")

        elif guess > number:
            print ("Too high! Try a lower number.")
    
    except ValueError:
     print("Invalid input. Please enter a whole number.")

if attempts == max_attempts:
    print(f"\nSorry! You ran out of tries. The number was {number}.")