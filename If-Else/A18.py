cp=int(input('Enter cost price: '))
sp=int(input('Enter selling price: '))
if sp>cp:
    print("Profit %:",((sp-cp)/cp)*100)
elif sp<cp:
    print("Loss %:",((cp-sp)/cp)*100)
else:
    print("No loss and Profit")
