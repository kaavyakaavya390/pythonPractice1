import inflect

names=[]
p=inflect.engine()
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        print("\nAdieu, adieu, to ",p.join(names))
        break
