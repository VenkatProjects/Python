class MyException(Exception):
    def __init__(self):
        super(Exception, self).__init__()
        self.args = ("Raised MyException",)


try:
    raise MyException()      
except MyException as ex:
    print(ex)