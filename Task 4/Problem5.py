#Rishwanth M
rows=int(input("Enter the Number of Rows:"))
for i in range(rows):
    for space in range(rows-i-1):
        print(end=" ")
    for asterisk in range(i+1):
        print("*",end=" ")
    print()
