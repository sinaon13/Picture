from PIL import Image
img = Image.open('1.jpg')
n=int(input("percent of opacue (multiples of 10) : "))
def sm(img,ij,fl,x,y):
    t=(0,0,0)
    p=-1
    for i in range(j):
        for k in range(j):
            p+=1
            t+=img.getpixel(x,y+i-p)
            t+=img.getpixel(x+i-p,y)
    
def op(img):
    weight = img.size[0]
    height = img.size[1]
    j=0
    fl=0
    for x in range(weight-1):
        l = []
        for y in range(height-1):
            if (x>1 and y>1) or (x<weight-1 and y>1) or (x>1 and y<height-1) or (x<weight-1 and y<height-1):
                t = img.getpixel((x+1, y-1))+img.getpixel((x-1, y+1))+img.getpixel((x-1, y-1))+img.getpixel((x+1, y))+img.getpixel((x, y+1))+img.getpixel((x, y-1))+img.getpixel((x-1, y))+img.getpixel((x+1, y+1))
            r=0
            b=0
            g=0
            for i in range(len(t)):
                if i%3==1:
                    r+=t[i]
                if i%3==2:
                    g+=t[i]
                if i%3==0:
                    b+=t[i]
            r=int(r/8)
            g=int(g/8)
            b=int(b/8)
            img.putpixel((x, y), (r, g, b))
img.save('2.jpg')
