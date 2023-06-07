class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print("init called")
    def __str__(self):
        print("str called")
        return "({0},{1})".format(self.x,self.y)
    def __add__(self,obj):
        print("add called")
        x=self.x+obj.x
        y=self.y+obj.y
        return Point(x,y)
p1=Point(10,20)
print(p1)
p2=Point(20,30)
print(p2)
print("addition of 2 object:",p1+p2)
