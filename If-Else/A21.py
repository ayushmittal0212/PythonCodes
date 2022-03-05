u=int(input("Enter units: "))
if 0<u<=50:
    tb=u*.5
elif u<=150:
    tb=50*.5+(u-50)*.75
elif u<=250:
    tb=50*.5+100.75+(u-150)*1.2
elif u>250:
    tb=50*.5+100*.75+100*1.2+(u-250)*1.5
tb=tb+tb*.2
print("Bill Amount:",tb)
