class fruits():
    def getfruits(self,n,name,rate):
        self.name=name
        self.rate=rate
        self.n=n

    def printFruits(self):
        print(self.name)
        print(self.rate)
        print(self.n)
        
onj_name=fruits()
num=1
i=int(input("enter the no of fruits you want"))


while (num<=i):
    fr=str(input("enter fruit"))
    n=input("enter the color of fruit")
    r=str(input("enter rate"))
    onj_name.getfruits(n,fr,r)

    num=num+1
    onj_name.printFruits()
        

     