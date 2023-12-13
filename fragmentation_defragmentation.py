from PIL import Image
import os


name = 'eyes.jpg'

im = Image.open(f"{name}")

N = 2 # разделить на N**2 = 4

for i in range(N):
    for j in range(N):
        if i!=N and j!=N:
            im.crop(box=(im.size[0]/N*i, im.size[1]/N*j, im.size[0]/N*(i+1)-1, im.size[1]/N*(j+1)-1)).\
            save(f'{name[:-4]}{str(i+1)}{str(j+1)}.jpg')

h = 10 # pixels # для визуализации
new_im = Image.new('RGB', (im.size[0]+3*h, im.size[1]+3*h), (0,0,0)) # (255,165,0) = orange

img = [[0] * (N) for _ in range(N)]
# print(img)

for i in range(N):
    for j in range(N):
        img[i][j] = Image.open(f'{name[:-4]}{str(i+1)}{str(j+1)}.jpg')
        # img[i][j].show()

new_im.paste(img[0][0], (0+h,0+h)) 
new_im.paste(img[1][0], (img[0][0].size[0]+2*h,0+h)) 
new_im.paste(img[0][1], (0+h,img[0][0].size[1]+2*h)) 
new_im.paste(img[1][1], (img[0][0].size[0]+2*h,img[0][0].size[1]+2*h)) 

for i in range(N):
    for j in range(N):
        os.remove(f'{name[:-4]}{str(i+1)}{str(j+1)}.jpg')
  
new_im.save(f'{name[:-4]}_merged.jpg', "JPEG") 
new_im.show()