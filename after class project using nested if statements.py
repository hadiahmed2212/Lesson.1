holiday_type= int(input("1 = bech type holiday 2 = mountain type holiday"))
if holiday_type == 1:
    beach_type = int(input("you chose beach holiday now choose if you want to pick swimming (1) or making a sandcastle(2)"))
    if beach_type == 1:
        print("you picked the resort beach holiday!")
    else:
        print("you picked the camping beach holiday!")
elif holiday_type == 2:
    mountain_type = int(input("you chose mountain holiday now choose if you want to pick camping (1) or hiking(2)"))
    if mountain_type == 1:
        print("your final decision was camping, enjoy your new camping trip!")
    else:
        print ("your final decison was hiking, enjoy your new hiking trip!")
if holiday_type != 1 and holiday_type != 2:
    print("ERROR WRONG INPUT!")