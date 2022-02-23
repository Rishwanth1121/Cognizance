#Rishwanth M
number=int(input("Enter The Number:"))
new_number=number
rev=0
while(number>=1):
    rem=number%10
    rev=(rev*10)+rem
    number=int(number/10)
if new_number==rev:
    print(new_number," Is A Palindrome Number")
else:
    print(new_number," Is Not A Palindrome Number")
    
