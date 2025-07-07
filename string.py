#Strings

message = """Bob's World is cool"""

print(message)

#Advanced concepts - Strings
message1 = 'Hello'

print(message1[0])
print(message1[1])

print(message1[-1])

message2 = ' Hello '

print(len(message2))

message3 = ' Hello World '

print(message3.strip()) # Remove leading and trailing whitespace
print(message3.lower()) # Convert all charaters to lowercase
print(message3.split(',')) # Split the string into a list based on the comma

#Numaric Data

num = 3

print(type(num))

num2 = 3.14

print(type(num2))

# int num = 3
# float num = 3

#Variables

my_variable = 10
total_count = 0
user = 'John'

#Invalid
second_variable = 10
user_name = 20

#Operators

#Add(+)
#Minus(-)
#Multiply(*)
#Division(/)
#Modulus(%)
#Exponents(**)

x = 10
y = 2

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(5%2)
print(x**y)

t = 10
t =t+2
t +=2
t -=2

print(t)

#Operators with strings

str1 = 'Hello'
str2 = 'World'

print(str1 + " " + str2)
print(str1 * 3)

#Control Statement

num3 = -5
num4 = 10

if num3 > 0:
    print("This number is positive")
elif num3 == 0:
    print("This number is zero")
else:
    print("This number is negative")

num5 = int(input("Enter the first number:"))
num6 = int(input("Enter the second number:"))

if num5 > num6:
     print(num5,"is greater than", num6)
elif num6 > num5:
    print(num6, "is greater than", num5)
else:
    print("Both numbers are equal")

#Loop

fruits = ["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)

numbers = [1, 2, 3, 4, 5, 7]

for number in numbers:
    print(number)

#Using a while loop to count from 1 to 5
count = 1

while count <= 5:
    print(count) 
    count += 1 # Increment the count by 1   

#Loop control statement

vegetables = ["carrots","cabbage","beetrot","date"]

for veges in vegetables:
    if veges == "beetrot":
        break #Exit the loop if beetrot is found
    print(veges)

print()

for veges in vegetables:
    if veges == "beetrot":
        continue #Skips beetrot and moves to the iteration
    print(veges)

for veges in vegetables:
    if veges == "beetrot":
        pass #Placeholder, no action is needed for beetrot
    print(veges)

count1 = 0

while count1 < 5:
    print(count1)
    count1 += 1
    if count1 == 3:
        break #Exits the loop when the count is reached - 3 
