total_100 = total_50 = total_20 = total_10 = total_5 = total_1 = 0
customers_served = 0
total_dispensed= 0
notes_dispensed = 0
serving=True
while serving:
    name=input("what is your name")
    print("welcome",name,)
    withdrawing= int (input("how much do you want to withdraw?"))
    if withdrawing <= 0:
        print("INVALID AMOUNT PLEASE TRY AGAIN,",name,)
        continue
    print(f"\nDispensing {withdrawing} units for {name}:")
    remaining = withdrawing
    i = 1
    while i <=6:
        if i == 1:
            value = 100
        elif i == 2:
            value = 50
        elif i == 3:
            value = 10
        elif i == 4:
            value = 5
        else:
            value = 1
        count = remaining // value
        if count >0:
