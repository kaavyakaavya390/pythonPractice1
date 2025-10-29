def func(name, age, location):
    print("Hello ,", name)
    print(f"age {age} , location {location}")
    location=[]


def func2(arg1, *arg2, **arg3):
    for i in arg2:
        print(i)
    arg2=list()
    for val in arg3:
        print(f"pairs : {val} -> {arg3[val]}")
    print("welcome!!!")


def main():
    func2(40, 30, 40, 50, apple=10, banana=30)
    func("default", 20, location=["coimbatore"])
    # name="user"
    # func(name)
    print("-----lambda------")
    f = lambda a: a + 1
    print(f(2))
    print(f(5))

    func3()


def func3():
    print("Thank you!!")


main()
