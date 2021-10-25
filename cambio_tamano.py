from PIL import Image
import os, sys
import glob

lis_imgjpg = glob.glob(r'C:\Users\jorge\Downloads\Photos/*.jpg')
for item in lis_imgjpg:
    print(item)
    basewidth = 600
    img = Image.open(item)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(item +' resized_image.jpg')