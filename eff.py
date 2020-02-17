from PIL  import Image
n=input('types: cold, warm')
img=Image.open(input('name: '))
def cold(img):
    width = img.size[0]
    height = img.size[1]
    for i in range(width):
        for j in range(height):
            (r,g,b)=img.getpixel((i,j))
            img.putpixel((i,j),(int(r/2),g,b))
    return img
img2=cold(img)
img2.save('2.jpg')
    
