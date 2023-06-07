class A:
    def show(self):
        print("show from class A")
class B(A):
    def show(self):
        super().show()
        print("show from class B")
class C(A):
    def show(self):
        super().show()
        print("show from class C")
class D(B,C):
    def show(self):
        super().show()
        print("show from class D")
b1=D()
b1.show()
