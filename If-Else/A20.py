bs=int(input('Enter basic salary: '))
if bs<=10000:
    ts=bs+bs*0.2+bs*0.8
elif bs<=20000:
    ts=bs+bs*.25+bs*.9
else:
    ts=bs+bs*.3+bs*.95
print("Total Salary:",ts)
