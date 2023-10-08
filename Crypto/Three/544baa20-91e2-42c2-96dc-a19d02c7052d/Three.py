import datetime
import numpy as np

class Protocol:
    def __init__(self,party_num):
        self.pn=party_num#party_num in 0,1,2

    def Read_Data(self,path):
        data=open(path).readline().strip()
        try:
            if('.' in data):
                data=float(data)
            else:
                data=int(data)
        except:
            print('No number')
            exit(-1)
        return data

    def Get(self,x1,x2):
        #The function of this function is to get two secret shared values
        pass

    def RGet(self,x1):
        #The function of this function is to obtain a secret shared value
        pass

    def ReShare(self,x):
        #let x=x+ri, where r0+r1+r2=0
        #ri, i=0,1,2 is a random integer
        #then, send x to part (self.pn+1)%3
        pass

    def Secret_Share(self,x):
        #Both x1 and x2 are random integers
        x3=x-x1-x2
        sharelist=[x1,x2,x3]
        loc=self.pn
        self.reserved=(sharelist[loc],sharelist[(loc+1)%3])
        return (sharelist[0],sharelist[1]),(sharelist[1],sharelist[2]),(sharelist[2],sharelist[0])

    def Mul_loc_compute(self,x1,y1,x2,y2):
        self.mulx=x1*y1+x1*y2+x2*y1

    def Add_loc_compute(self,x1,y1):
        self.addx=x1+y1

    def Cyberslacking(self):
        print('Cyberloafing!!')
        print('Cyberloafing!!')
        print('Cyberloafing!!')

    def Save_Data(self):
        #This is a default and optional function
        #Compress all data once rebuild the function's answer
        pwd=str(datetime.datetime.now())
        pass

    def Func(self,expression):
        print('Math expression',expression,'will be computed! You can get the answer without leak your privacy!')

    def ReBuild(self,x1,x2,x3):
        #Rebuild the function's answer from secret sharing values
        return x1+x2+x3

#A0 is the 'flag{xxxxxxxxxxx' and X0 is xxxxx...xxx B0 is xxxxxxxxx}
#A(party 0) has A0, B(party 1) has X0 and C(party 2) has B0
#Function is A0*X0+B0
p0=Protocol(0)
p1=Protocol(1)
p2=Protocol(2)