def load_text(filename):
    with open(filename, "r") as f:
        return f.read()

def write_text(filename, text):
    with open(filename, "w") as f:
        f.write(text)
        return True

import os
import pathlib
filepath = pathlib.Path("D:\dev\puzzles", "decoded-0-Eighty-NineCiphertexts.txt")
print(filepath)
originaltext = str(load_text(filepath))
# for i in range(0, 20):
#     print(originaltext[i])
newtext = ""

""" def get_next_letter(index):
    # on even indices, read from front
    # on odd indices, read from back
    if index % 2 == 0:
        #even index
        return originaltext[int(index/2)]
        
    elif index % 2 == 1:
        #odd index
        return originaltext[int(-(index-1)/2)]

for i in range(0, 10):...
    nextletter = get_next_letter(i)
    newtext.append(nextletter)

print(str(newtext))
 """
def insertChar(mystring, position, chartoinsert ):
    mystring   =  mystring[:position] + chartoinsert + mystring[position:] 
    return mystring   

#Inserting some characters with a defined position:    
# print(insertChar(a,0, '-'))    
# print(insertChar(a,9, '@'))    
# print(insertChar(a,14, '%'))   

numchars = len(originaltext)
# for i in range(0, numchars):
    # insertChar(newtext, i, "!")
    # newtext += "!"
    # newtext[i] = "!"
newtext = ""
fwd = 0
bck = numchars - 1
next = fwd
for i in range(0, numchars):
    newtext += originaltext[next]
    if i % 2 == 0:
        fwd += 1
        next = bck
    else:
        bck -= 1
        next = fwd

# print(newtext[:20])
filename = "decoded-1.txt"
write_text(filename, newtext)