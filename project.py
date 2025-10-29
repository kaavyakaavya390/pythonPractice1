# main_module.py

import re
import requests
import sys
import random
from datetime import date, datetime
from collections import Counter
import emoji
import inflect
from num2words import num2words
import pyfiglet
from PIL import Image, ImageOps
import validators
import csv
from tabulate import tabulate


# ----------------- Emoji / Text -----------------
def convert_emojis(statement):
    return statement.replace(":)", "\U0001f642").replace(":(", "\U0001f641")


def emojize_text(text):
    return emoji.emojize(text, language="alias")


# ----------------- Einstein -----------------
def einstein_energy(mass):
    return mass * pow(3e8, 2)


# ----------------- String to Float -----------------
def to_float(val):
    return float(val.strip("$"))


def per_to_float(val):
    return float(val.strip("%")) / 100


# ----------------- Meal Time -----------------
def meal_time_convert(time):
    h, m = time.split(":")
    return float(h) + float(m)/60


# ----------------- Cola Machine -----------------
def cola_machine(amount=50, coins=[]):
    for coin in coins:
        if coin not in [5, 10, 25]:
            continue
        if coin >= amount:
            return coin - amount
        else:
            amount -= coin
    return amount


# ----------------- TWTTR -----------------
def twttr(string):
    vowels = "aeiouAEIOU"
    return "".join(c for c in string if c not in vowels)


# ----------------- Number Plate -----------------
def plate_check(val):
    if not (2 <= len(val) <= 6):
        return "Invalid"
    i = 0
    while i < len(val) and val[i].isalpha():
        i += 1
    if i == 0 or i == len(val):
        return "Invalid"
    if val[i:].isdigit():
        return "Valid"
    return "Invalid"


# ----------------- Fuel -----------------
def fuel_status(i):
    v1, v2 = map(int, i.split("/"))
    res = int((v1/v2)*100)
    if res >= 99:
        return "F"
    elif res <= 1:
        return "E"
    return f"{res}%"


# ----------------- Jar -----------------
class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self.n = 0

    def __str__(self):
        return "🍪" * self.n

    def deposit(self, n):
        if n < 0:
            raise ValueError("n should be non-negative")
        if self.n + n > self._capacity:
            raise ValueError("Exceeds capacity")
        self.n += n

    def withdraw(self, n):
        if self.n - n < 0:
            raise ValueError("Not enough cookies")
        self.n -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.n


# ----------------- IP Validation -----------------
def is_valid_ip(ipid):
    pattern = r"^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"
    return bool(re.match(pattern, ipid))


# ----------------- Bitcoin Price -----------------
def bitcoin_cost(n, api_key=None):
    url = "https://rest.coincap.io/v3/assets/bitcoin"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    price_usd = float(data["data"]["priceUsd"])
    return n * price_usd


# ----------------- Hours Conversion -----------------
def convert_hours(s):
    pattern = r"^([1-9]|1[0-2])(:[0-5][0-9])?\s(AM|PM)\sto\s([1-9]|1[0-2])(:[0-5][0-9])?\s(AM|PM)$"
    match = re.fullmatch(pattern, s)
    if not match:
        raise ValueError("Invalid format")
    start_hour, start_min, start_period, end_hour, end_min, end_period = match.groups()
    start_min = start_min[1:] if start_min else "00"
    end_min = end_min[1:] if end_min else "00"
    start_hour = int(start_hour)
    end_hour = int(end_hour)
    start_24 = to_24(start_hour, start_min, start_period)
    end_24 = to_24(end_hour, end_min, end_period)
    return f"{start_24} to {end_24}"


def to_24(hour, minutes, period):
    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12
    return f"{hour:02}:{minutes}"
