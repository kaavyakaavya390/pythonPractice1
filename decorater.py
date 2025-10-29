def my_decarater(func):
    print(f"decorater running...{func}")
    def wrapper(*args):
        print(f"{args}")
        print("the function starts....")
        value=func(*args)
        print("The function ended.....")
        return value
    return wrapper
@my_decarater
def func(*name):
    return f"Hiiii {name}"
print(func("Kaviya","Anitha","Pallavi"))

#---------------------------------
class mystatic:
    def __init__(self,func):
        self.__func__=func
    
    def __get__(self,obj,cls=None):
        print("decorater")
        return self.__func__
class myclass:
    var=45
    def __init__(self,val):
        self.val=val
    @mystatic
    def call():
        print("my class.........")

obj=myclass(10)
print(obj.__dict__)
myclass.call()