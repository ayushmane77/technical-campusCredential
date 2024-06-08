class studentINfo():
    def providedetails(self,name,age):
        self.name=name
        self.age=age
    def getdetails(self):
        print(self.name)
        print(self.age)
    
obj_name=studentINfo()
obj_name.providedetails("Ayush",21)  
obj_name.getdetails()         