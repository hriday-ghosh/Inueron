"""
1.	What are the two values of the Boolean data type? How do you write them?
Ans - Boolean can have two values: true and false,
A = True
B = False
C = (1 == 3)
Print(C)

2.	What are the three different types of Boolean operators?
Ans - True or False basically.
AND, OR, and NOT


3. Make a list of each Boolean operator's truth tables(i.e. every possible combination of Boolean values for the operator and what it evaluate).
Ans-
x = 5
y = 8

print("x == y:", x == y)
print("x != y:", x != y)
print("x < y:", x < y)
print("x > y:", x > y)
print("x <= y:", x <= y)
print("x >= y:", x >= y)
x == y: False
x != y: True
x < y: True
x > y: False
x <= y: True
x >= y: False


4. What are the values of the following expressions?
(5 > 4) and (3 == 5)
If both conditions are true then this statement will work.
not (5 > 4)
(5 > 4) or (3 == 5)
If any conditions are true then this statement will work.
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)
5. What are the six comparison operators?
Ans - Python has six comparison operators, which are as follows:
Less than (< )
Less than or equal to (<= )
Greater than (> )
Greater than or equal to (>= )
Equal to (== )
Not equal to (!= )

6. How do you tell the difference between the equal to and assignment operators? Describe a condition and when you would use one.
Ans - The ‘==’ operator checks whether the two given operands are equal or not .
"=" It is an assignment operator.

Inputs = input("Enter Student Name: ")
Student_Names = [["Ram", 95], ["Shyam", 85]]
if Inputs == "Ram":
    print(f"Ram's no is {Student_Names[0][1]}")
else:
    print("Students is no mathed")
if Inputs == "Shyam":
    print(f"Shyam no is {Student_Names[1][1]}")
else:
    print("Students is no mathed")


7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')

Ans-
1st Block
spam = 0
if spam == 10:
print('eggs')
2nd Block
if spam > 5:
print('bacon')
3rd Block
else:
print('ham')
print('spam')
print('spam')

8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
spam = input("Enter your no or character:- ")

if spam == "1":
    print('Hello')
elif spam == "2":
    print('Howdy')
else:
    print('Greetings!')


9. If your programme is stuck in an endless loop, what keys you’ll press?
Ans - Ctrl + C in Terminal if you are using in VS Code.
10. How can you tell the difference between break and continue ?
Ans-
Continue:
If we use continue then the whole condition would be skipped.
Break:
When we use break then, it will be out from the loop if the condition once true, and never enter in the loop again.

11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
Ans - range(10)


for i in range(10):
    print(i)
It means it would print 0 to 9
range(0, 10)

for i in range(0, 10):
    print(i)

Here 0 means starting index and 10 means the last index would be 9
range(0, 10, 1)

for i in range(0, 10, 1):
    print(i)
It means, the starting index would be 0 and print till 9 and 1 index would be jumping index. Means if we start with 0 index then it would go till 5th index and 4th index would be printed and between 1-4th index would be avoided.

12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
Ans - 1st question
for i in range(1, 11):
    print(i)
By Do while:

i = 0
while i <= 9:
    i = i+1
    print(i)

13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
Ans - spam.bacon()

"""
