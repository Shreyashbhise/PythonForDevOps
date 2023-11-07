# Get the score from the user
score = float(input("Enter the score: "))

# Check the score and assign a grade
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Display the grade
print("Your grade is {}".format(grade))
