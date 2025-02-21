#1.	Write a program to find the largest of two numbers using if-else statements.
#number1 = 20
#number2 = 50
#if(number1 > number2):
 #   print(number1,"is largest",number2)
#else:
 #   print(number2,"is largest",number1)

number1 = int(input("Enter the number1 :"))
number2 = int(input("Enter the number2 :"))
if number1 > number2 :
    print("The largest value is number1",number1)
elif number1 == number2 :
    print("The number are the same")
else:
    print("The largest value is number2",number2)
    



