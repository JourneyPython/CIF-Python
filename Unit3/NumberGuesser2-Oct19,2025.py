import random

wins = 0
losses = 0
retries = 5
game_count = 0

while game_count < retries:
    attempts = 0
    max_attempts = 3

    print("\n<<<<WELCOME TO THE GUESSING GAME>>>>")
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))

    if lower_bound >= upper_bound:
        print("Invalid range. The lower bound must be less than the upper bound.")
        continue

    elif lower_bound == upper_bound - 1:
        print(f"The only possible number is {lower_bound}. You win by default!")
        wins += 1
        game_count += 1
        continue

    else:
        print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
        print(f"You have {max_attempts} attempts to guess the number.")

    number = random.randint(lower_bound, upper_bound)

    while attempts < max_attempts:
        try:
            guess = int(input(f"Your guess (integer between {lower_bound} and {upper_bound}): "))
            if not (lower_bound <= guess <= upper_bound):
                print(f"Please guess a number within the range of {lower_bound} to {upper_bound}.")
                continue

            attempts += 1   

            if guess == number:
                print(f"Congratulations! You guessed the number {number} in {attempts} attempt(s).")
                wins += 1
                break 

            elif guess < number:
                print("Too low! Try a higher number.")

            elif guess > number:
                print("Too high! Try a lower number.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")
    
        if attempts == 2:
                hint = random.choice(['even/odd', 'divisible3', 'divisible5'])

                if hint == 'even/odd':
                    if number % 2 == 0:
                        print("Hint: The number is even.")
                        
                    else:
                        print("Hint: The number is odd.")

                elif hint == 'divisible3':
                    if number % 3 == 0:
                        print("Hint: The number is divisible by 3.")

                    else:
                        print("Hint: The number is NOT divisible by 3.")

                elif hint == 'divisible5':
                    if number % 5 == 0:
                        print("Hint: The number is divisible by 5.")

                    else:
                        print("Hint: The number is NOT divisible by 5.")

    if attempts == max_attempts and guess != number:
        print(f"\nSorry! You ran out of tries. The number was {number}.")
        losses += 1

    game_count += 1
    print(f"Games played: {game_count}/{retries}.")

    if game_count < retries:
        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if play_again != "yes":
            break
    
print(f"\nYou played {game_count} game(s) out of {retries}.")
print("\nThanks for playing!")
print(f"Final score: {wins} win(s), {losses} loss(es). \nGoodbye!")