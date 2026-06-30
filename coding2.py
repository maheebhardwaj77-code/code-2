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

