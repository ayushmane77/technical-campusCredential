class evenNumbers():
    def even(self,a):
        self.a=a
        sum=0
        sum+=a
        print("sum",sum)
        

    def odd(self,a):
        self.a=a
        product=1
        product=product*self.a
        print("pro",product)

num=evenNumbers()


n=int(input("emter the range"))
for i in range(1,n+1):
    if i%2==0:
       

       num.even(i)
    else:
        num.odd(i)    



         