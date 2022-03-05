a=int(input("Enter month no.: "))
if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
    print("Month has 31 days")
elif a==4 or a==6 or a==9 or a==11:
    print("Month has 30 days")
elif a==2:
    print("Month has 28 days")
else:
    print("Invalid!!!")