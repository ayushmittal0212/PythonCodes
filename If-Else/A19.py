p=int(input('Enter Physics Marks: '))
c=int(input('Enter Chem Marks: '))
m=int(input('Enter Maths Marks: '))
b=int(input('Enter Bio Marks: '))
cs=int(input('Enter CS Marks: '))
pc=((p+c+m+b+cs)/500)*100
print("Percentage:",pc)
if pc>=90:
    print("Grade: A")
elif pc>=80:
    print("Grade: B")
elif pc>=70:
    print("Grade: C")
elif pc>=60:
    print("Grade: D")
elif pc>=40:
    print("Grade: E")
else:
    print("Grade: F")