s1=int(input('Enter 1st side: '))
s2=int(input('Enter 2nd side: '))
s3=int(input('Enter 3rd side: '))
if s1<=s2+s3 and s2<=s3+s1 and s3<=s1+s2:
    print("Valid ",end='')
    if s1==s2==s3:
        print("Equilateral ",end='')
    if s1==s2 or s2==s3 or s3==s1:
        print("Isoscales ",end='')
    if s1**2==s2**2+s3**2 or s2**2==s3**2+s1**2 or s3**2==s1**2+s2**2:
        print("Right Angled ",end='')
else:
    print("Invalid ",end='')
print("Triangle")