print("Application")

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Welcome", name)
print("Your age is", age)

if int(age) >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

print("Application finished")
