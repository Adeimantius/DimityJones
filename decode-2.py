### File Mangement Operations
def load_text(filename):
    with open(filename, "r") as f:
        return f.read()

def write_text(filename, text):
    with open(filename, "w") as f:
        f.write(text)
        return True

### Imports
import os
import pathlib

### Input Text
path_root = "D:/dev/puzzles/DimityJones/"
in_filename = "puzzle-2.txt"
in_filepath = pathlib.Path(path_root, in_filename)
print(in_filepath)
input_text = str(load_text(in_filepath))
# for i in range(0, 20):
#     print(input_text[i])

### Output Text
out_text = ""


### Last Solution
""" 
def insertChar(mystring, position, chartoinsert ):
    mystring   =  mystring[:position] + chartoinsert + mystring[position:] 
    return mystring   

#Inserting some characters with a defined position:    
# print(insertChar(a,0, '-'))    
# print(insertChar(a,9, '@'))    
# print(insertChar(a,14, '%'))   

numchars = len(input_text)
# for i in range(0, numchars):
    # insertChar(newtext, i, "!")
    # newtext += "!"
    # newtext[i] = "!"
newtext = ""
fwd = 0
bck = numchars - 1
next = fwd
for i in range(0, numchars):
    newtext += input_text[next]
    if i % 2 == 0:
        fwd += 1
        next = bck
    else:
        bck -= 1
        next = fwd
"""

inputlist = input_text.split(".")
newlist = []
for line in inputlist:
    correctline = line.split(" ")
    correctline.reverse()
    newlist.append(" ".join(correctline))

out_text = ".".join(newlist)


#print(out_text)
print(out_text[:100])

### Dump text to file
out_filename = "solution-2.txt"
write_text(out_filename, out_text)