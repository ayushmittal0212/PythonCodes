s1=int(input('Enter 1st side: '))
s2=int(input('Enter 2nd side: '))
s3=int(input('Enter 3rd side: '))
if s1<=s2+s3 and s2<=s1+s3 and s3<=s1+s2:
    print("Valid Triangle")
else:
    print("Not a valid Triangle")
    