
#Creating exception handling fucntion 

print("\n This script will throw the raised exception error\n")

class MyException(Exception):
    def __init__(self):
        super(Exception, self).__init__()
        self.args = ("Raised MyException",)

try:
    raise MyException()      
except MyException as ex:
    print(ex)
