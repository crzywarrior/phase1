#IF CONDITION:
'write a prgrm in which u taken int i/p frm user. if tht int , if it is divisible by 3 and 6 than print good number, if the int is divisible by 2 and 7 than print an avg number, if the number is divisible by 4 or 9 than print awosome number else print bads number'

'''a=int(input('enter the number:'))
if((a%3==0)&(a%6==0)):
    print('good number')
elif((a%2==0)&(a%7==0)):
    print('avg number')
elif((a%4==0)|(a%9==0)):
    print('awsome number')
else:
    print('bad number')'''

'write a prgrm to check the on-road price of a bike under the conditions if the price is greater than 72k than income taxes is 10% of the original price and insurance will be 15% actual price; if the price is greater than 1.5L and less than 2L, the tax would be 25% and the insurance will be 20%; if the price is above 2L than tax will be 35% and insurance will be 28%; otherwise if ur amount is not support the price is less than 72K, enter a valid value(actual_value+tax+insurance).'

'''price=int(input('enter the price:'))
if((price>72000)and(price<150000)):
    tax=(price/100)*10
    print('tax:',tax)
    insurance=(price/100)*15
    print('insurance:',insurance)
elif((price>150000)and(price<200000)):
    tax=(price/100)*25
    print('tax:',tax)
    insurance=(price/100)*20
    print('insurance:',insurance)
elif(price>=200000):
    tax=(price*35)/100
    print('tax:',tax)
    insurance=(price/100)*28
    print('insurance:',insurance)
else:
    print('enter the valid amount')    
total=(price+tax+insurance)
print('total amount',total)'''

'''check if a number is leap or not if the year is divisible by 4 & not divisible by 100.
  i) OR      ii)Divisible by 400 print leap year'''

'''year=int(input('enter year:'))
if((year%4==0)and(year%100!=0)):
   print('leap year')
elif((year%400==0)):
   print('leap year')
else:
   print('enter positive year')'''

'~ write a prgrm to check the type of triangle where you take the i/p frm user for 3 sides and classified accordingly  into equilateral & isolater(any 2 sieds equal) & scaling(no 2 sides are equal).'

'''a=int(input('enter the side a:'))
b=int(input('enter the side b:'))
c=int(input('enter the side c:'))
if(a==b==c):
    print('equilatent')
elif((a==b)or(b==c)or(c==a)):
    print('isolatent')
else:
    print('scaling')'''

#LOOPS:

#FOR 

'~ calculate the value of 7 factorial using for loop.'

'''a=int(input('enter value:'))
fact=1
for i in range(a,1,-1):
    fact*=i
print(fact)'''

'~ print first 10 fibonic series.'

'''a=0
b=1
print(a)
print(b)
for i in range(3,11):
    c=a+b
    print(c)
    a=b
    b=c'''

'~ print the given number is prime or not.'

'''n=int(input('enter the value:'))
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        break
if(flag==1):
    print('not')
else:
    print('prime')'''

#WHILE
'calculate the sum of digits of a number which is taken as i/p frm user.'








