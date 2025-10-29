from collections import Counter

#--------change input to lowercase-------
name = input("enter anything : ")
name = name.lower().upper()
print(name)

#-------change "  " ->  "..."-------------
input2 = input("enter string to change space -> ... : ")
input2 = input2.replace(" ", "...")
print(input2)


# ---------convert :) -> 🙂--------------
def convert(statement):
    return statement.replace(":)", "\U0001f642").replace(":(", "\U0001f641")


# ------E=mc^2---------
def einstain(mass):
    return mass * pow(300000000, 2)


# -------functions to change from string to float------
def to_float(val):
    return float(val.strip("$"))


def per_to_float(val):
    return float(val.strip("%")) / 100


# ----------42---------
def deep():
    val = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? "
    )
    if val == "42" or val.lower() == "forty-two" or val.lower() == "forty two":
        return "YES"
    return "No"


# ---------Meal Time------------
def mealTimeconvert(time):
    h, m = time.split(":")
    h = float(h)
    m = float(m)
    return h + (m / 60.0)


# -----coco cola------
def cola():
    amount = 50
    print("Amount due : ", amount)
    while True:
        coin = int(input("insert coin : "))
        if coin == 10 or coin == 25 or coin == 5:
            if coin >= amount:
                print("change Owed : ", coin - amount)
                break
            else:
                amount -= coin
        print("Amount due : ", amount)


# ------vowels twttr-------
def twttr(string):
    # string = input("Input : ")
    vowels = "aeiouAEIOU"
    res = ""
    for c in string:
        if c not in vowels:
            res += c
    return res

#------number plate----
def platecheck(val):
    # val = input("Input: ")
    if not (2 <= len(val) <= 6):
        return "Invalid"
    i = 0
    while i < len(val) and val[i].isalpha():
        i += 1
    
    if i == 0 or i == len(val):
        return "Invalid"
    
    if val[i:].isdigit():
        return "Valid"
    else:
        return "Invalid"

#------------ fruits calories-----
def fruits():
    fruit_calories_lower = {
    'apple': 130,
    'avocado': 50,
    'banana': 110,
    'cantaloupe': 50,
    'grapefruit': 60,
    'grapes': 90,
    'honeydew melon': 50,
    'kiwifruit': 90,
    'lemon': 15,
    'lime': 20,
    'nectarine': 60,
    'orange': 80,
    'peach': 60,
    'pear': 100,
    'pineapple': 50,
    'plums': 70,
    'strawberries': 50,
    'sweet cherries': 100,
    'tangerine': 50,
    'watermelon': 80
    }
    friut=input("Item : ")
    try:
        print("calories : ",fruit_calories_lower[friut])
    except KeyError:
        pass


#-------fuel check-------
def fuel(i):
    v1,v2=i.split("/")
    try:
        v1=int(v1)
        v2=int(v2)
        while True:
            try:
                res=int((v1/v2)*100)
            except Exception:
                raise Exception
            else:
                if res>=99:
                    return "F"
                elif res<=1:
                    return "E"
                else:
                    return f"{res}%"
    except Exception:
        pass

#-------- Taqueria items----------
def Taqueria():
    items={
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
    }
    total=0.0
    while True:
        try:
            item=input("Item : ")
            if item.lower() in items.keys():
                total+=items[item]
                print("Total : $",total)
            else:
                continue
        except EOFError:
            print("\n")
            break
        except ValueError:
            continue
        
#-------grocery---------
def grocery():
    items=[]
    while True:
        try:
            items.append(input().upper())
            continue
        except EOFError:
            res=Counter(items)
            res=dict(sorted(res.items()))
            for it in res.keys():
                print(f"{res[it]} {it}")
            break
        except Exception:
            continue
#------date format------
def dateFormat():
    month = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()
            m, d, y = 0, 0, 0

            if "/" in date: 
                m, d, y = date.split("/")
                m = int(m)
                d = int(d)
                y = int(y)

            elif "," in date: 
                parts = date.replace(",", "").split()
                if len(parts) != 3:
                    raise ValueError
                m_name, d, y = parts
                if m_name not in month:
                    raise ValueError
                m = month.index(m_name) + 1
                d = int(d)
                y = int(y)

            else:
                raise ValueError

            if 1 <= m <= 12 and 1 <= d <= 31 and len(str(y)) == 4:
                print(f"{y}-{m:02}-{d:02}")
                break
            else:
                raise ValueError

        except ValueError:
            continue
#--------greetings---------
def bankgreetig(string):
    # -------greetings-------
    greeting =string.lower()

    if greeting.startswith("hello"):
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"

def main():
    print(deep())
    input3 = input("enter str with :) or :( : ")
    input3 = convert(input3)
    print(input3)

    input4 = int(input("m : "))
    print(einstain(input4))

    # -------Meal Time------
    time = input("What time is it? ")
    timeval = mealTimeconvert(time)
    if timeval >= 7.0 and timeval <= 8.0:
        print("breakfast time")
    elif timeval >= 12.0 and timeval <= 13.0:
        print("Lunch time")
    elif timeval >= 18.0 and timeval <= 19.0:
        print("Dinner time")
    else:
        pass
    # --------meal------------
    amount = to_float(input("How much was the meal? "))
    percent = per_to_float(input("What percentage would you like to tip? "))
    print(f"Leave ${(amount*percent):.2f}")

 

    # ---(f"{float(eval(exp)):.1f}")
    # -----------expression evaluation---------
    exp = input("enter expression : ")
    print(f"{float(eval(exp)):.1f}")

    # --------Coco Cola---------
    cola()

    # ------twttr----------
    print(twttr())

    #------number plate-----
    print(platecheck())

    #----fruits-----
    fruits()

    #----fuel-----
    fuel()

    # -------items order-------
    Taqueria()
    
    #---------grocery-------
    grocery()

    #--------date format------
    dateFormat()
    twttr("rabbit")

main()
