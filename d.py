# WAP to find the greater Number
n1=int(input("Enter a Number:"))
n2=int(input("Enter a Number:"))
n3=int(input("Enter a Number:"))
if n1 > n2:
    if n1 > n3:
        print("n1 is greater")
    else:
        print("n3 is greate")
else:
    if n2 > n3:
        print("n2 is greater")
    else:
        print("n3 is greater")