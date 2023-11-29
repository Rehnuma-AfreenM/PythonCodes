maximum_marks = float(input("enter the total maximum marks of all subjects : "))
sub1 = int(input("Enter marks of the first subject: "))
sub2 = int(input("Enter marks of the second subject: "))
sub3 = int(input("Enter marks of the third subject: "))
sub4 = int(input("Enter marks of the fourth subject: "))
sub5 = int(input("Enter marks of the fifth subject: "))
sum = float(sub1 + sub2 + sub3 + sub4 + sub5)
print("The sum is :", sum)
percentage = (sum / maximum_marks) * 100
print("the percentage is : ", percentage)
if percentage >= 90:
    print("Grade: A+")

elif percentage >= 70 and percentage < 90:
    print("Grade: A")

elif percentage >= 60 and percentage < 75:
    print("Grade: B")

elif percentage >= 45 and percentage < 60:
    print("Grade: C")

elif percentage >= 33 and percentage < 45:
    print("Grade: D")

elif percentage > 33:
    print("Grade: E")
