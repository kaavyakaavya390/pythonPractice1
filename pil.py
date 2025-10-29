from PIL import Image

with Image.open("/home/kaviya-pt7969/Downloads/Untitled.jpg") as im:
    # im.show()
    box = (0, 0, 64, 64)
    region = im.crop(box)
    region = region.transpose(Image.Transpose.ROTATE_180)
    im.paste(region, box)
    # im.show()
    out = im.rotate(180)
    out.show()
