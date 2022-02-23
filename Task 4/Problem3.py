#Rishwanth M
n=int(input('Enter The Number of Students : '))
a=[['Roll Number','Name','Marks']]
for i in range(n):
    rollno=input('Enter Roll Number : ')
    studentname=input('Enter Student Name : ')
    marks=int(input('Enter Marks : '))
    a.append([rollno,studentname,marks])
for i in range(len(a)):
    for j in range(len(a[i])):
        k=a[i][j]
        print(k,end='\t')
    print('\n')
h=int(input('Enter the Row to be Printed : '))
for i in a[h]:
    print(i,end='\t')
