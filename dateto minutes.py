import sys
from datetime import date , datetime
from num2words import num2words
try:
    birthday=input("Date(YYYY-MM-DD) : ").strip()
    birthdate=datetime.strptime(birthday, "%Y-%m-%d").date()
    print(birthdate)
    diff=(date.today())-birthdate
    print(diff.days)
    totalminutes=diff.days * 24 * 60
    print(totalminutes)
    inwords=num2words(totalminutes)
    print(f"{inwords}")
except ValueError:
    print("Enter in correct format....")