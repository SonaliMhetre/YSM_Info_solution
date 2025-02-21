#Write a program that prints the grade based on the score input using if-else statements (A for 90-100, B for 80-89, etc.).

sub1 = 60
sub2 = 60
sub3 = 60
sub4 = 60
sub5 = 60
score = (sub1+sub2+sub3+sub4+sub5)/5
if 90 <= score <= 100:
    print("grade = A")
elif 80 <= score <= 89:
    print("grade = B")
elif 70 <= score <= 79:
    print("grade = C")
elif 60 <= score <= 69:
    print("grade = D")
elif 0 <= score <= 59:
    print("grade = F")
else:
    print(grade = "Invalid score")



sub01 = int(input("Enter the marks : "))
sub02 = int(input("Enter the marks : "))
sub03 = int(input("Enter the marks : "))
sub04 = int(input("Enter the marks : "))
sub05 = int(input("Enter the marks : "))
score = (sub01+sub02+sub03+sub04+sub05)/5
if 90 <= score <= 100:
    print("grade = A")
elif 80 <= score <= 89:
    print("grade = B")
elif 70 <= score <= 79:
    print("grade = C")
elif 60 <= score <= 69:
    print("grade = D")
elif 0 <= score <= 59:
    print("grade = F")
else:
    print(grade = "Invalid score")