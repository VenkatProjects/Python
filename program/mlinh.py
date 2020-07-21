class A:
    def printA(self):
        print("from A")

class B:
      def printB(self):
        print("from B")

class C(A,B):
      def printC(self):
        print("from C")


obj = C()

obj.printA()
obj.printB()
obj.printC()

