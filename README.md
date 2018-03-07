
>~~ How to use ~~ 
to hide your message in image:
1. put your picture in /
2. put your message in /messages
3. run encode.py
e.g. python encode.py image.jpg secret.txt
(it will search for secret in /messages by default)

to unhide message from an image:
1. put an image in /
2. run decode.py
e.g. python decode.py _image.jpg
3. The hidden message will appear in cmd and 
   can be found in /encoded

>~~ Directories
encoded - contains messages read from images
messages - here program search for your messages to encode
logs - selfexplanatory
>~~ Python files
peel.py - contains important modules 
encode.py - use this to hide your message in picture
decode.py - use to show hidden messages from pictures
