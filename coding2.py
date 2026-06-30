print("hello guys")
A = int(input("A :"))
G = input("M OR F :")
if((A == 1 or A == 2) and G == "M"):
    print("fee is 100")

elif(A == 3 or A == 4 or G == "F"):
    print("fee is 200")

elif(A == 5 and G == "M"):
    print("fee is 300")

else:
    print("no fee") 

#Single Line Conditional Statements:-
age = int(input("age :"))
vote = "yes can give vote" if age >= 18 else "no you can't give vote"
print(vote)

#Clever If statements:-
marks = int(input("marks :"))
result = ("fail", "pass")  [marks >= 40]
print(result)

#Type Casting:-
a = 4
b = "5"
c = int(b)
sum = a + c
print(sum)

#WAP a program to input 2 number and print their sum:-
num1 = int(input("num1 :"))
num2 = int(input("num2 :"))
addition = num1 +num2
print("the addition of these two number is :",addition) 

#WAP to input side of a square and print its area:-
side = int(input("side :"))
permeter = 4 * side
area = side * side
print("the permeter of square is :",permeter)
print("the area of square is :", area)

#WAP to input 2 floating point number and print their average:-
numf1 = float(input("numf1 :"))
numf2 = float(input("numf2 :"))
average = (numf1 + numf2) / 2
print("the average is :",average)

#WAP to input 2 int number a and b. Print true if a is greater than or equal to b. If not print false:-
first = int(input("first :"))
second = int(input("second :"))
print(first >= second)     