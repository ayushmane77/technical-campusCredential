class area():
    def getRadius(self,r):
        self.r=r
    def printArea(self):
        print(3.14*(self.r)*(self.r)) 

obj_name=area()
obj_name.getRadius(4)
obj_name.printArea()           