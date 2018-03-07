from __future__ import print_function
from PIL import Image
import pprint

pp = pprint.PrettyPrinter()

class Peeler:
    def __init__(self, name):
        # load picture
        try:
            self.imname = name
            self.im = Image.open(name)
            print("image opened")
        except IOError as e:
            print("file cannot be opened")

    def __call__(self):
        im = self.im
        print(im.format, im.size, im.mode)

    def save(self):
        self.im.save(''.join(("_",self.imname)), format="BMP")

    def makeFingerprint(self):
        name = self.imname.split(".")[0]
        self.fpname = ''.join(('fp', name, '.fpk'))
        try:
            f = open(self.fpname, 'w')
        except FileNotFoundError:
            f = open(self.fpname, 'w')
        for line in self.im.getdata():
            f.write(''.join((str(line),'\n')))
        f.close()

class ImageEnkoder:
    def __init__(self, pr, bw):
    #bw is BinaryIterator object
        fp = []
        for x,y,z in pr.im.getdata():
            #pp.pprint(format(z,'08b'))
            try:
                z = int(''.join((format(z,'08b')[:6], bw.__next__())), 2)
                #pp.pprint((z, int(z,2)))
                fp.append((x,y,z))
            except StopIteration as e:
                break

        pr.im.putdata(fp)
        pr.makeFingerprint()
        pr.save()


class BinaryIterator:
    def __init__(self, word):
        self.word = word

        #get binary from characters
        array = [format(ord(i), '08b') for i in word]
        self.binary = ''.join(array)
        self.length = len(self.binary)
        self.blength = format(self.length, '08b')
        array = [self.blength] + array
        self.binary = ''.join(array)

        #print(self.word,'\n',self.binary)
        
        #iteration
        self.current = 0
        
        #pp.pprint(array)
        
    def __call__(self):
        print(self.binary)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            #get two next bytes
            self.r = ''.join((self.binary[self.current],self.binary[self.current+1]))
        except Exception as e:
            raise StopIteration
                  
        self.current += 2
        return self.r


class ImageDekoder:
    def __init__(self, im):
        self.message = ''
        self.im = im
        self.len = ''
        i = 0
        for x,y,z in im.getdata():
            if not (i<4):
                break
            self.len += format(z,'08b')[6:]
            i+=1
        self.len = int(self.len ,2)
        #print(self.len)
        i = 4
        for x,y,z in im.getdata():
            if not (i<(self.len/2)+8):
                break
            self.message += format(z,'08b')[6:]
            i+=1
        #print(self.message)

    def decode(self):
        i = 1
        buff = []
        self.damessage = []
        self.dmessage = ''
        for b in self.message:
            buff.append(b)
            if(i%8==0):
                self.damessage.append(buff)
                buff = []
            i+=1
        for char in self.damessage:
            self.dmessage += chr(int(''.join(char),2))
            #print(char)
        self.dmessage = self.dmessage[1:] #because first bytes represents len
        return self.dmessage

# how to use
#bw = BinaryIterator("hello world xaxaxa xd")

#pr = Peeler('_image.jpg')
#IE = ImageEnkoder(pr,bw)
#ID = ImageDekoder(pr.im)
#print(ID.decode())
