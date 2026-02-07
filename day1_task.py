a=int(input("enter a value:"))
i=1
print(a%2 == 0 and "number is even" or "number is odd")
while i<=a:
    if i%2==0:
        print(i)
    elif i%2!=0:
        print(i)
    i=i+1