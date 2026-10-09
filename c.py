List_1= [1,2.1,3,"Mango",4,5.1,6,"Lichi"]
total = 0
for X in List_1:
    if type(X) == int:
        total = total + X
print(f"sum of intiger value is {total}")
