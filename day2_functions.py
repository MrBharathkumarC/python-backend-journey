def greet(name):
    return( f"Hello, {name}")

print(greet("Bharath"))


def add(a, b):
    return a + b

print(add(5, 10))


def is_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even(7))




numbers = [10, 20, 30, 40, 50]

numbers.append(60)
numbers.remove(20)

print(numbers)

for n in numbers:
    print(n)

marks = [35, 67, 89, 45, 90]

for m in marks:
    if m >= 40:
        print(m, "Pass")
    else:
        print(m, "Fail")
