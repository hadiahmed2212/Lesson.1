chores_pending=4
print("you have",chores_pending," pending chores.")
chores_completed=0
chores_num=1
while chores_num<= chores_pending:
    if chores_num==1:
        next_c="do the laundry"
    elif chores_num==2:
        next_c="do your bed"
    elif chores_num==3:
        next_c="mop the floor"
    else: next_c="wash the dishes"
    chores_fins= (input(f"have you finished {next_c} ?"))
    if chores_fins == "no":
        print("finish your chores then come back")
    else:
        print("nice, you finished your chores.")
        chores_completed+= 1
        chores_num+= 1
    print("chores remaining are ",chores_pending- chores_completed,)
print("HORRAY, you completed all yur chores now you can ask your mum for a PS5")
print()
print("total work today", chores_pending,)
print("you did this amount of chores:",chores_completed,)
print("remaining chores:", chores_pending- chores_completed)