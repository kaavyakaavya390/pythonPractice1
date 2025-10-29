import pyfiglet
import sys
f="standard"
try:
    text=input()
    if len(sys.argv)>1:
        if sys.argv[1]!="-f" and sys.argv[1]!="--font":
            raise Exception
        f=sys.argv[2]
    out=pyfiglet.figlet_format(text,font=f)
    print(out)
except Exception as e:
    print(e)
        