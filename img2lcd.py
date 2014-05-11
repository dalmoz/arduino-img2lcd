# script for transforming images into LCD bitcode
# output is suitable for Arduino LCD import 
def pxl2lcd(pxllst):
    bitStr = "B"
    delim = ",\nB"
    for px in range(0,len(pxllst)):
        bitStr += str(pxllst[px])
        if px != 0:
            if px % 5 == 4:
                bitStr += delim
    bitStr = bitStr[:-2]
    bitStr += "\n},\n{\n"
    return bitStr

import Image
# change image filename
imgFile = "c:\\temp\\image.png"

img = Image.open(imgFile)
imgg = img.convert("1")

bitBlock = "const uint8_t charBitmap[][8] = {\n{\n"

for j in [0,1]:
    topy = j * 8
    for i in range(0,15):
        topx = i * 5    
        timg = imgg.crop([topx , topy, topx + 5, topy + 8])
        croplst = timg.getdata()
        croplstt = [1 if e == 0 else e for e in croplst]
        croplsf =  [0 if e == 255 else e for e in croplstt]
        bitBlock += pxl2lcd(croplsf)
bitBlock = bitBlock[:-4]
bitBlock += "\n};"

print bitBlock
