# variables
name = "Bharath"
age = 22
is_graduate = True

print(name)
print(age)
print(is_graduate)

# input from user
city = input("Enter your city: ")
print("You are from", city)
marks = int(input("Enter your marks: "))

if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First class")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")

for i in range(1, 6):
    print("Number:", i)
