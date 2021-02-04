from PIL import Image, ImageDraw
import math
import random
import selenium
bar_length=input("barcode length:\n>> ")
seperators=input("number of seperators (usually 3):\n>> ")
barnums=[]
bar_pixels=17
if int(bar_length)>50:
    bar_pixels=8
if int(seperators)>0:
    pixelx=((bar_pixels+1)*(6+((int(seperators)-2)*5)+(7*int(bar_length))))
else:
    pixelx=((bar_pixels+1)*(7*int(bar_length)))
pixely=pixelx#math.ceil(pixelx/3.6643437863)
numcodes=[[3,2,1,1],[2,2,2,1],[2,1,2,2],[1,4,1,1],[1,1,3,2],[1,2,3,1],[1,1,1,4],[1,3,1,2],[1,2,1,3],[3,1,1,2]]
for i in range(int(bar_length)):
    if int(seperators) > 0 and((i==0)):
        barnums.append([0,0,1,1,1])
    elif int(seperators) > 2 and i>0 and i!=(int(bar_length)-1) and (i%math.ceil(int(bar_length)/(int(seperators)-1))==0):
        barnums.append([1,1,1,1,1])
    randomNumber=random.randint(0, 9)
    print(randomNumber)
    barnums.append(numcodes[randomNumber])
    if int(seperators) > 0 and i==(int(bar_length)-1):
        barnums.append([0,0,1,1,1])

img = Image.new('RGB', (pixelx,pixely), 'white')
draw = ImageDraw.Draw(img)
x=0
oddeven=0
for barnum in barnums:
    if len(barnum)==5:
        y = math.ceil(pixely * .9)
    else:
        y = math.ceil(pixely * .5)
    for bar in barnum:
        if bar!=0:
            if oddeven%2==0:
                fillcolor=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            else:
                fillcolor=(255,255,255)
            draw.rectangle([x,0,x+(bar*bar_pixels),y],fill=fillcolor)
            oddeven += 1
            x += (bar*bar_pixels)+1

img=img.crop((0,0,x,pixely))
img.save('barcode.png')