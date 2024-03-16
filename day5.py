#INHERITANCE

'''class Faculty:#parent class
    def __init__(self,f_name,department,f_id):
        self.f_name=f_name
        self.department=department
        self.f_id=f_id
    def print_info(self):
        print('faculty information:',self.f_name,self.department,self.f_id)
obj=Faculty('bheem','cse',1264)
obj.print_info()'''

#multi-level
''''class placements:
    def info(self,count):
        self.no=count
        print('we have',self.no,'placements this year and stilll counting....')

class department(placements):
    def display(self,list):
        list=['IT','CSE','EEE','ECE','ME','CE']
        print('we have the departments listed below')
        for i in list:
             print(i)

class pragati(department):
        def welcome(self):
            print('welcome to the pragati engineering college')
pec=pragati()
pec.welcome()
pec.info(1150)
pec.display(list)'''

#multiple
'''class placements:
    def info(self,count):
        self.no=count
        print('we have',self.no,'placements this year and stilll counting....')

class department:
    def display(self,list):
        list=['IT','CSE','EEE','ECE','ME','CE']
        print('we have the departments listed below')
        for i in list:
             print(i)

class pragati(placements,department):
        def welcome(self):
            print('welcome to the pragati engineering college')
pec=pragati()
pec.welcome()
pec.info(1150)
pec.display(list)'''

#polymorpahasn
'''class arithmatic:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a*b+c)
obj=arithmatic()
obj.add(10)
obj.add(10,20)
obj.add(1,2,3)'''

#ABSTRACTION

from abc import ABC,abstractmethod
class ticket(ABC):
    @abstractmethod
    def book_ticket(self):
        pass

class makemytrip(ticket):
    def details(self,name,contact,mail,journey_date):
        self.n=name
        self.c=contact
        self.m=mail
        self.j=journey_date
        n=input('enter your name:')
        c=int(input('enter mobile number:'))
        m=input('enter mail id')
        j=input('enter the journey date:')
        print('Thank you for booking from makemytrip.\n')

class Irctc(makemytrip):
    w=input('please choose the trip mode:\none way round way\n')

    while True:
        if w=='one way':
            print('Thank you for choosing IRCTC')
            break
        elif w=='round way':
            r=input('enter the return date of your journey:')
            break
        else:
            print('invalid')
        break

class indigo(Irctc):
    t=input('please choose transport mode:\n1.train 2.bus 3.flight\n')
    print('Thank you for choosing indigo.')

    while True:
        if t=='train' or t=='flight' or t=='bus':
            print('Thank you for choosing IRCTC')
            break
        else:
            print('invalid')
        break
obj=makemytrip()
obj.book_ticket()