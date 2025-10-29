# -------my Error  class------
class MyCustomError(Exception):
    def __init__(self, message="the number should be in between 1 and 9!!!"):
        # self.num = num
        self.message = message
        super().__init__(self.message)


class ForException:
    # -----Chaining try-------
    def chaining(self):
        try:
            open("nofile.txt")
        except OSError:
            raise RuntimeError("unable to handle error")

    # ----------Nested try block-------
    def Nested_try(self):
        try:
            a = int(input("enter a : "))
            b = int(input("enter b : "))
            try:
                res = a / b
                print(f"value is : {res}")
            except Exception:
                raise ZeroDivisionError
            finally:
                print("<<<Nested try block>>>")
        except ZeroDivisionError as e:
            e.add_note("Notes : Enter b with non zero value")
            print("b must be non zero value....", e.__notes__)
        except ValueError:
            print("Enter integer only.........")
        finally:
            print("<<<outer try block>>>")

    # --------try except-------
    def check(self, num):
        if num < 1 or num > 9:
            raise MyCustomError(num)

    def pow(self):
        while True:
            try:
                num = int(input("enter the value(between 1 to 9): "))
                self.check(num)
                print(f"square value of {num} : ", pow(num, 2))
                break
            except ValueError as e:
                print("enter the integer only.....")
                continue
            except MyCustomError as m:
                print(f"the number you entered : {num} >>> {m.message}")
                continue


class B(Exception):
    def __init__(self, message="Error B"):
        self.message = message
        super().__init__(self.message)


class C(B):
    def __init__(self, message="Error C"):
        self.message = message
        super().__init__(self.message)


class D(C):
    def __init__(self, message="Error D"):
        self.message = message
        super().__init__(self.message)


def main():
    # obj = ForException()
    # # obj.chaining()
    # obj.Nested_try()
    # for cls in [B, C, D]:
    # try:
    #     raise cls()
    # except D as e:
    #         print("D", e.message)
    # except C as e:
    #         print("C", e.message)
    # except B as e:
    #         print("B", e.message)
    # num=input("enter value:")
    try:
        num=3/"d"
    except  TypeError as e:
        print(e.args)
    finally:
        print("exeption block...")



# File: example.py

# def a():
#     b()

# def b():
#     c()

# def c():
#     d = 1 / 0

# a()
import sys
import traceback

def might_fail():
    return 1 / 0

try:
    might_fail()
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    tb_list = traceback.extract_tb(exc_traceback)
    last_call = tb_list[-1]  # Get the last frame in the list
    line_number = last_call.lineno
    # print(f"The exception occurred on line {line_number}")
    print(tb_list)
    print(tb_list[-1])
    print(tb_list[-1].lineno)

# Output:
# The exception occurred on line 5



# main()
