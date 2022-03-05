amt=int(input('Enter the amount: '))-100
print("2000 notes:",amt//2000)
amt%=2000
print("500 notes:",amt//500)
amt%=500
print("200 notes:",amt//200)
amt%=200
print("100 notes:",(amt//100)+1)

