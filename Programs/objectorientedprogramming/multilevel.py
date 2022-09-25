class P1:
    def m1(self):
        print("inside m1")
class P2(P1):
    def m2(self):
        print("inside m2")
class P3(P2):
    def m3(self):
        print("inside m3")
p3=P3()
p3.m3()
p3.m2()
p3.m1()