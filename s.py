from PIL import Image
img = Image.open('1.jpg')
n=int(input("percent of opacue (multiples of 10) : "))
def sm(img,j,x,y):
    t=(0,0,0)
    p=-1
    l=-1
    for i in range(j):
        l+=1
        for k in range(j):
            p+=1
            g1=t[0]            
            g2=t[1]
            g3=t[2]
            t=(g1+img.getpixel((x+p-j,y+l-j))[0],g2+img.getpixel((x+p-j,y+l-j))[1],g3+img.getpixel((x+p-j,y+l-j))[2])
    g1=t[0]/(j**2)          
    g2=t[1]/(j**2) 
    g3=t[2]/(j**2) 
    t=(g1,g2,g3)
    return t
def op(img,n):
    weight = img.size[0]
    height = img.size[1]
    for x in range(weight-1):
        for y in range(height-1):
            if (x>n and y>n) or (x<weight-n and y>n) or (x>n and y<height-n) or (x<weight-n and y<height-n):
                (r,g,b)=sm(img,n,x,y)
            img.putpixel((x, y), (r, g, b))
    return(img)
img=op(img,n)
img.save('2.jpg')
