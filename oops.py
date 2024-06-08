class calculator:
    def add(self,a,b):
        self.a=a
        self.b=b
    # def  addition(self):
        print(self.a+self.b)    
    def subtract(self):
        print(self.a-self.b)  
    def multiply(self):
        print(self.a*self.b) 
    def divide(self):
        print(self.a/self.b)          
obj_name=calculator()
obj_name.add(12,23)  
obj_name.subtract()   
obj_name.divide()  
# obj_name.addition(1,2) 
# sachin=calculator()
# sachin.add()
