from __future__ import print_function
from os import path
from peel import Peeler, BinaryIterator, ImageEnkoder
import sys

# python encode image.jpg secret.txt
try:
    print('Image: ', sys.argv[1])
    print('Secret: ', sys.argv[2])
except IndexError:
    pass

image = sys.argv[1]
secret = sys.argv[2]
#image = 'image.jpg'
#secret = 'secret.txt'

#read secret message
fpath = path.join('messages', secret)
f = open(fpath, 'r')
smessage = ''
for x in f:
    smessage += x
f.close()


bi = BinaryIterator(smessage)
pr = Peeler(image)
pr()
IE = ImageEnkoder(pr,bi)
print("Image saved as _"+image)
    
