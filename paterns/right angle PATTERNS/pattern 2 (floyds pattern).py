rows = int(input("how many rows do you want"))
number = 1
for i in range (1,rows+1):
    for j in range (1, i+1):
        print(number,end= " " )
        number = number + 1
    print()
