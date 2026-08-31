s = float(input("Enter the score: "))
if s > 100 or s < 0:
    print("Invalid score. Please enter a score between 0 and 100.")
elif s >= 90:
    print("Grade: A")
elif s >= 80:
    print("Grade: B")
elif s >= 70:
    print("Grade: C")
elif s >= 60:
    print("Grade: D")
else:
    print("Grade: F")