def twttr(string):
    # string = input("Input : ")
    vowels = "aeiouAEIOU"
    res = ""
    for c in string:
        if c not in vowels:
            res += c
    return res