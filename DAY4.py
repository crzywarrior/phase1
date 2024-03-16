#LISTS
#write a prgrm to find the 2nd smallest -ve no. frm list without sort(),min(),max().
#l=[22,-1,42,65,1,-4,6]
'''m1=l[0]
m2=l[0]
for i in range(len(l)):
    if m1>l[i]:
        m1=l[i]
for i in range(len(l)):    
    if m2>l[i] and m1!=l[i]:
        m2=l[i]
print(m2)'''

'''def find_second_smallest_negative(lst):
    smallest = float('inf')
    second_smallest = float('inf')

    for num in l:
        if num < 0:
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif num < second_smallest:
                second_smallest = num

    return second_smallest
result = find_second_smallest_negative(l)
print(f"The second smallest negative number is: {result}")'''

'''m1=999
m2=999
for i in range(len(l)):
    if l[i]<m1:
        m2=m1
        m1=l[i]
print(m2)'''

'''l=[22,15,42,-4,1,-1]
m1=999
m2=999
for i in range(len(l)):
    if l[i]<m1:
        m2=m1
        m1=l[i]
    elif m1>l[i] and m2>m1:
        m2=l[i]
print(m2)'''

#MEMORY ALLOCATION

#SETS

#{2,0,1024,0,40,230,0} shift all 0's to right end side while maintaining the right order.

#l=[2,0,1024,0,40,230,0]

#OOPS FUNCN:

#create a clss f15 with funcn's lights,fans and a/c.
#when lights func is called it's prints out the color of the light which is taken as parameter to the funcn.
#when fan func is called it displays the regulator spd, which is taken as the parameter of the funcn.
#when a/c displays the current room temp. and the outside temp. which are taken as parameters.
#who's name is display which displays the diff in outside and room temp. in a/c and aslo displays the fan spd.

'''class f15:
    def light(self,color):
        self.color=color
        print('color of light:',color)
    def fan(self,spd):
        self.spd=spd
        print('regulator spd:',spd)
    def ac(self,room,ots):
        self.room=room
        self.ots=ots
        print('current room temp:',room)
        print('current outside temp:',ots)
    def display(self,room,ots,spd):
        print('diff temp:',ots-room)
        print('current fan spd:',spd)

o=f15()
o.light('red')
o.fan(4)
o.ac(34,50)
o.display(34,50,4)'''

'''class f15:
    def light(self,color):
        self.clr=color
        print('color of light:',color)
    def fan(self,spd):
        self.sp=spd
        print('regulator spd:',spd)
    def ac(self,room,ots):
        self.rm=room
        self.ot=ots
        print('current room temp:',room)
        print('current outside temp:',ots)
    def display(self,room,ots,spd):
        diff=self.ot-self.rm
        print('diff temp:',diff)
        print('current fan spd:',spd)

o=f15()
o.light('red')
o.fan(4)
o.ac(34,50)
o.display(34,50,4)'''

#CONSTRUCTOR

'''class interview:
    def __init__(self):
        p=1150
        print('placements:',p,'in pragati')
place=interview()'''

'''class f15:
    def __init__(self,k,l):
        a=150
        print('total students:',a)
        self.a=k
        self.b=l
    def light(self):
        print('light:',self.a)
        print('fan:',self.b)


p=f15(30,15)
p.light()'''


#2nd FUNCN: who's varient. according to the car company name and car model, the  user should be ask to enter the varient, he would like to choose from petrol,diesel.
#3rd FUNCN: display fucn: according to the car company car model name and car varient 1st it's ex-showroom price should displayed and than it's on-road price should displayed, which is calculated as ex-showroom price+CGST+SGST+insurance. all the have the common value for the car company.

class crzycars:
    def __init__(self):
        print('WELCOME TO CRZYCARS:\nchoose one from the Brands:\n1.Toyota 2.Mahindra 3.Mercedes 4.exit')

    def brand(brnd):
        #brnd.bnd
        t='toyota';m='mahindra';mr='mercedes'
        b=(input('Enter the car Brand:'))
        while True:
            if b=='toyota' or b==1:
                print('we have limited models\n1.innova 2.urbanz 3.etios 4.back')
                mdl1='innova';mdl2='urbanz';mdl3='etios';mdl4='back'
                mdl=input('choose from them:')
                if mdl==mdl1:
                    print('choose varient:\n1.petrol 2.diesel 3.hybrid')
                    var1='petrol';var2='diesel';var3='hybrid';var4='back'
                    var=input('choose from them:')
                    if var==var1:
                        exshowroom1=100000
                        print('ex-showroom price:',exshowroom1)
                        onroadprice(100000)
                        break
                    elif var==var2:
                        exshowroom2=150000
                        print('ex-showroom price:',exshowroom2)
                        onroadprice(150000)
                        break
                    elif var==var3:
                         print('ex-showroom price:')#,exshowroom
                        #onroadprice()
                    elif var!=var1 or var2 or var3:
                        print('sorry,sir')
                        break
                    elif var==var4:
                        break
                elif mdl!=mdl1:
                    print('sorry,sir')
                    break
                elif mdl==4 or mdl=='back':
                    break
            elif b!='toyota' or b!=1:
                print('sorry,sir')
                break
            elif b==4:
                break
        
            elif b=='mahindra' or b==1:
                print('we have limited models\n1.thar 2.XUV700 3.bolero 4.back')
                mdl1='thar';mdl2='XUV700';mdl3='bolero';mdl4='back'
                mdl=input('choose from them:')
                if mdl==mdl1:
                    print('choose varient:\n1.petrol 2.diesel 3.hybrid')
                    var1='petrol';var2='diesel';var3='hybrid';var4='back'
                    var=input('choose from them:')
                    if var==var1:
                        print('ex-showroom price:')#,exshowroom
                        #onroadprice()
                    elif var==var2:
                        print('ex-showroom price:')#,exshowroom
                        #onroadprice()
                    elif var==var3:
                         print('ex-showroom price:')#,exshowroom
                        #onroadprice()
                    elif var!=var1 or var2 or var3:
                        print('sorry,sir')
                        break
                    elif var==var4:
                        break
                elif mdl!=mdl1:
                    print('sorry,sir')
                    break
                elif mdl==4 or mdl=='back':
                    break
            elif b!='toyota' or b!=1:
                print('sorry,sir')
                break
            elif b==4:
                break

            elif b=='mercedes' or b==1:
                print('we have limited models\n1.s class 220id 2.m class m5 550d 3.a class AMG 4.back')
                mdl1='s class 220id';mdl2='m class m5 550d';mdl3='a class AMG';mdl4='back'
                mdl=input('choose from them:')
                if mdl==mdl1:
                    print('choose varient:\n1.petrol 2.diesel 3.hybrid')
                    var1='petrol';var2='diesel';var3='hybrid';var4='back'
                    var=input('choose from them:')
                    if var==var1:
                        print('ex-showroom price:')#,exshowroom
                        #onroadprice()
                    elif var==var2:
                        print('ex-showroom price:')#,exshowroom
                        #onroadprice()
                    elif var==var3:
                         print('ex-showroom price:')#,exshowroom
                        #onroadprice()
                    elif var!=var1 or var2 or var3:
                        print('sorry,sir')
                        break
                    elif var==var4:
                        break
                elif mdl!=mdl1:
                    print('sorry,sir')
                    break
                elif mdl==4 or mdl=='back':
                    break
            elif b!='toyota' or b!=1:
                print('sorry,sir')
                break
            elif b==4:
                break
    def onroadprice(n):
        print('\nThe showroom price of the car is : ',n)
        cgst=n*10/100
        sgst=n*10/100
        insurance=n*15/100
        total=n+cgst+sgst+insurance
        print('The total price of the car includes :\nCGST(10%)=',cgst,'\nSGST(10%)=',sgst,'\nINSURANCE(15%)=',insurance,'\nTOTAL PRICE = ',total)
    print()
    brand()
            

cars=crzycars()
cars.brand()
cars.onroadprice()