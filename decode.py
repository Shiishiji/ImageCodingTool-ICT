from __future__ import print_function
import sys
from peel import Peeler, ImageDekoder
from os import path

# python encode image.jpg secret.txt
try:
    print('Image: ', sys.argv[1])
    #print('Secret: ', sys.argv[2])
except IndexError:
    pass

image = sys.argv[1]


pr = Peeler(image)

ID = ImageDekoder(pr.im)
msg = ID.decode()
print(msg)

#read secret message
#and save to file.txt
ipath = path.join('encoded', image.split('.')[0]+'-encoded.txt')
f = open(ipath, 'w')

f.write(msg)
f.close()

