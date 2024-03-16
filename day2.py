#I/p 12345

#digits
'''n=12345
while(n!=0):
    r=n%10
    print(r)
    n=n//10
'''

#no of the digits in a number
'''n=12345
c=0
while(n!=0):
    r=n%10
    c=c+1
    n=n//10
print('The no of the digits are: ',c)
'''
#sum of the digits in a number
'''n=12345
sum=0
while(n!=0):
    r=n%10
    sum=sum+r
    n=n//10
print('The sum of the digits are: ',sum)
'''

#product of the digits in a number
'''n=12345
p=1
while(n!=0):
    r=n%10
    p=p*r
    n=n//10
print('The product of the digits are: ',p)

n=int(input('enter the number : '))
temp=n
sum=0
while(n!=0):
    r=n%10
    sum=sum+r
    n=n//10
if temp%sum==0:
    print(' number is divisible by its sum of digits')
else:
    print(' number is not divisible by its sum of digits')

s1=0
s2=0
for i in range(1,31):
    if i%6==0:
        s1=s1+i
    else:
        s2=s2+i
if s1>s2:
    d=s1-s2
else:
    d=s2-s1
print('value:',d)

#palindrome number

n=int(input('enter the number : '))
temp=n
rev=0
while(n!=0):
    r=n%10
    rev=rev*10 + r
    n=n//10
if temp==rev:
    print('PALINDROME NUMBER!')
else:
    print('NOT A PALINDROME NUMBER!')

# Define the number of rows
rows = 7

# Upper half of the diamond
for i in range(rows):
    if i <= rows // 2:
        for j in range(rows - i - 1):
            print(" ", end=" ")
        for k in range(2*i + 1):
            print("*", end=" ")
    else:
        for j in range(i - rows // 8):
            print(" ", end=" ")
        for k in range(2*(rows - i) - 1):
            print("*", end=" ")
    print()

n=int(input('value:'))
count=0;temp=0;sum=0;
a=0;b=0;c=0;

str_n = str(n)
n_digits = len(str_n)
print('len:',len(str_n))

for i in str_n:
    sum += int(i) ** n_digits
print('sum:',sum)

if sum == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")

#1578= 1*1 + 52 + 73 + 8*4

n=int(input('Enter the number : '))
c=0
temp=n
while(n!=0):
    c=c+1
    n=n//10
p=c
sum=0
while(temp!=0):
    r=temp%10
    sum=sum+r**p
    p=p-1
    temp=temp//10
print('the answer is : ',sum)

# Online Python - IDE, Editor, Compiler, Interpreter

n=8
for i in range(n):
    for s in range(n-i):
        print("",end=' ')
    if i%2!=0:
        for j in range(i):
            print('*',end=' ')
    print()
print()
n=5
for i in range(n,0,-1):
    for s in range(n-i):
        print("",end=' ')
    if i%2!=0:
        print(end='   ')
        for j in range(i):
            print('*',end=' ')
    print()'''

#I/p 12345

#digits
'''
n=12345
while(n!=0):
    r=n%10
    print(r)
    n=n//10
'''

#no of the digits in a number
'''
n=12345
c=0
while(n!=0):
    r=n%10
    c=c+1
    n=n//10
print('The no of the digits are: ',c)
'''

#sum of the digits in a number
'''
n=12345
sum=0
while(n!=0):
    r=n%10
    sum=sum+r
    n=n//10
print('The sum of the digits are: ',sum)
'''

#product of the digits in a number
'''
n=12345
p=1
while(n!=0):
    r=n%10
    p=p*r
    n=n//10
print('The product of the digits are: ',p)
'''

#take an integer an ip from user and check wether if the number is divisible by its sum of digits or not

'''
n=int(input('enter the number : '))
temp=n
sum=0
while(n!=0):
    r=n%10
    sum=sum+r
    n=n//10
if temp%sum==0:
    print(' number is divisible by its sum of digits,Harshad Number')
else:
    print(' number is not divisible by its sum of digits')
'''

#take a number input from user check if the sum of factors of that number is greater than the original number or not
#if yes print yes else no
'''
n= int(input('Enter the number '))
sum=0
for i in range(1,n/2+1):
    if n%i==0:
        sum=sum+i
if sum>n:
    print('yes,abandant')
else:
    print('no')
'''       

#calculate the difference of sum of numbers that are divisible by 6 and not divisible by 6 in the range of first 30 numbers

'''
s1=0
s2=0
for i in range(1,31):
    if i%6==0:
        s1=s1+i
    else:
        s2=s2+i
if s1>s2:
    d=s1-s2
else:
    d=s2-s1
print('the difference of sum of numbers that are divisible by 6 and not divisible by 6 in the range of first 30 numbers:',d)

'''

#palindrome number

'''
n=int(input('enter the number : '))
temp=n
rev=0
while(n!=0):
    r=n%10
    rev=rev*10 + r
    n=n//10
if temp==rev:
    print('PALINDROME NUMBER!')
else:
    print('NOT A PALINDROME NUMBER!')

'''

#Armstrong number

'''
n=int(input('enter the number : '))
temp1=n
temp2=n
c=0
while(temp1!=0):
    r=temp1%10
    temp1=temp1//10
    c=c+1
sum=0
while(temp2!=0):
    r=temp2%10
    sum=sum+r**c
    temp2=temp2//10
if sum==n:
    print(n,'is Armstorng number')
else:
    print(n,'is not Armstorng number')
'''

#1578= 1*1 + 52 + 73 + 8*4

'''n=int(input('Enter the number : '))
c=0
temp=n
while(n!=0):
    c=c+1
    n=n//10
p=c
sum=0
while(temp!=0):
    r=temp%10
    sum=sum+r**p
    p=p-1
    temp=temp//10
print('the answer is : ',sum)'''

#print the pattern given below:
#  *
#  * *
#  * * *
#  * * * *
#  * * * * *

'''for i in range(6):
    for j in range(i):
        print('*',end=' ')
    print()'''

#print the pattern given below:
#  * * * * *
#  * * * *
#  * * *
#  * * 
#  *

'''n=6
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()
    n=n-1'''

'''n=6
for i in range(n):
    for j in range(n,i,-1):
        print('*',end=' ')
    print()
    '''

#print the pattern given below:
#          *
#        * *
#      * * *
#    * * * *
#  * * * * *
'''n=6
for i in range(n):
    for s in range(n-i):
        print(" ",end=' ')
    for j in range(i):
        print('*',end=' ')
    print()
'''

#print square pattern
'''n=9
for i in range(1,n):
    for j in range(1,n):
        if (i==1 or i== n-1) or (j==1 or j==n-1):
           print('*',end=' ')
        else:
             print(' ',end=' ')
    print()

'''

#print the pattern given below:
#  1
#  2 3
#  4 5 6
#  7 8 9 10
#  11 12 13 14 15
'''n=1
for i in range(6):
    for j in range(i):
        print(n,end=' ')
        n=n+1
    print()
'''


#print the pattern given below:
#      *
#    * * *
#  * * * * *
#* * * * * * *
'''n=8
for i in range(n):
    for s in range(n-i):
        print("",end=' ')
    if i%2!=0:
        for j in range(i):
            print('*',end=' ')
    print()
'''

#print the pattern given below:
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5
#4 4 4 4
#3 3 3
#2 2
#1

for i in range(1,6):
    for j in range(i):
        print(i,end=' ')
    print()
for i in range(4,0,-1):
    for j in range(i):
        print(i,end=' ')
    print()
