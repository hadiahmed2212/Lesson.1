vehicle = int(input("1= bicycle 2= car"))
if vehicle== 1:
    vehicle_type = int(input("you chose bicycle now choose if you want to pick a tricicle(1) or normal bicycle(2)"))
    if vehicle_type ==2:
        print("you picked the normal bicycle!")
    else:
        print("you picked the tricycle!")
elif vehicle==2:
     vehicle_type = int(input("you chose car now choose if you want to pick a SUV(1) or sedan(2)"))
     if vehicle_type ==2:
         print("your final decision was sedan, enjoy your new sedan!")
     else:
         print ("your final decison was SUV, enjoy your new SUV!")
else:
    print("ERROR WRONG INPUT!")