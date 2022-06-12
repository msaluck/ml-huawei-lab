# Determine the entered score.
# input(): Receive input data.
score = input("Please enter your score.") # The input function receives input, which is a string. 
score = float(score) # Convert the score to a number. 
# try: except Exception: ... is a Python statement used to capture exceptions. If an error occurs in the statement in try, the statement in except is executed.
try:
    if 100>=score>=90: # Check whether the entered value is greater than the score of a level.
        print("Excellent") # Generate the level when conditions are met.
    elif 90 > score >= 80:
        print("Good")
    elif 80>score>0:
        print("Medium")
    else:
        print("Bad")
except Exception:
    print("Enter a correct score.") 

