import sys
import os
from PIL import Image , ImageOps
 
try:
    if len(sys.argv)!=3:
        sys.exit("Too few command-line arguments!!")
    infile=sys.argv[1]
    outfile=sys.argv[2]

    validext=[".jpg",".png",".jpeg"]
    inputext=os.path.splitext(infile)[1].lower()
    outext=os.path.splitext(outfile)[1].lower()
    if inputext not in validext or outext not in validext:
        sys.exit("files should be in following extension (.jpg/.png/.jpeg)")
    
    if inputext != outext:
        sys.exit("input and output must be same type!!!")

    image1=Image.open(infile)
    shirt=Image.open("shirt.png")

    image1=ImageOps.fit(image1,shirt.size)
    image1.paste(shirt,shirt)
    image1.save(outfile)

except FileNotFoundError:
    sys.exit("File is not there....")

