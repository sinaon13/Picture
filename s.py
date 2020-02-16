from PIL import Image
img = Image.open(input('picture name: ')+'.jpg')
n=int(input("contrast percent (multiple of 10) : "))
print('please wait ...')
def sm(img,j,x,y):
    t=(0,0,0)
    p=-1
    l=-1
    g1=0
    g2=0
    g3=0
    for i in range(j+2):
        p+=1
        l=-1
        for k in range(j+2):
            l+=1
            f=img.getpixel((x+p-j,y+l-j))
            t=(f[0],f[1],f[2])
            g1+=t[0]            
            g2+=t[1]
            g3+=t[2]
    g1=int(g1/((j+2)**2))
    g2=int(g2/((j+2)**2) )
    g3=int(g3/((j+2)**2) )
    t=(g1,g2,g3)
    return t
def op(img,img2,n):
    weight = img.size[0]
    height = img.size[1]
    for x in range(n+1,weight-n):
        for y in range(n+1,height-n):
            if (x>n and y>n) or (x<weight-n and y>n) or (x>n and y<height-n) or (x<weight-n and y<height-n):
                (r,g,b)=sm(img,n,x,y)
            img2.putpixel((x,y), (r, g, b))
    return(img2)
img2=img
im=op(img,img2,int(n/10))

im.save(input('transfered picture name: ')+'.jpg')
