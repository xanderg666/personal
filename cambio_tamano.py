from PIL import Image
import os, sys
import glob

path = r"C:\Users\jorge\Downloads\Photos (1)"
path = os.path.abspath(path)
dirs = os.listdir( path )

# Directory
directory = "convertidas"

# Parent Directory path
parent_dir = path

# Path
path1 = os.path.join(parent_dir, directory)

os.mkdir(path1)
print("Directory '% s' created" % directory)

lis_imgjpg = glob.glob(parent_dir + '/*.jpg')

for item in lis_imgjpg:
    # print(item)
    basewidth = 600
    img = Image.open(item)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    # extraer nombre del archivo
    nomb = os.path.basename(item)

    print(path1 + "/" + nomb)
    # guardar en la carpeta de convertidas
    img.save(path1 + "/" + nomb)
