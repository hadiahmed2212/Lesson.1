math= int(input("enter the marks you got for maths"))
english= int(input("enter the marks you got for english"))
HASS= int(input("enter the marks you got for HASS (history)"))
average=(math+english+HASS)//3
print("your average is:",average)
if average in range(30,40):
    print("c+")
elif average in range (41,60):
    print("b+")
else: print("A++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")