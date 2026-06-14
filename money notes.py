amount=int(input("enter an amount"))
note1=amount//100
remainder1=amount%100
note2=remainder1//50
remainder2=remainder1%50
note3=remainder2//10
print("100 rupee notes are",note1)
print("50 rupee notes are",note2)
print("10 rupee notes are",note3)