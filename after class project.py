print("welcome to the library visit planner, we will ask some questions please answer them correctly.")
weather_type= int(input("1 for sunny 2 for cloudy 3 for rainy weather"))
if weather_type==1:
    print("you should wear shorts and a short sleeve shirt to your library visit. ")
if weather_type==2:
    print("you should wear pants and a short sleeve shirt, if the clouds are grey ,pack an umbrella in case of rain.")
if weather_type==3:
    print ("pack an umbrella and wear a raincoat if its raining, BEWARE OF PUDDLES IF YOUR WALKING. ")
    if weather_type>=4:
        print("ERROR WRONG INPUT PLEASE TRY AGAIN!")
day_tdy=int(input("what is the day today enter the number of the day."))
if day_tdy>=6:
    print("check the library is open if it is then go.")
else:
    print("the library is open today")
if day_tdy>=8:
    print("ERROR WRONG INPUT!")
