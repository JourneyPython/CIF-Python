score = int(input("Enter Tom's score: "))

# Determine the result based on the score
if score == 100:
    print("tom did perfect!!")
elif score >= 90:
    print("tom did very well.")
elif score >= 80:
    print("tom did well.")
elif score >= 60:
    print("tom passed!")
elif score <= 60:
    print("tom failed.")