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
in_filename = "decoded-1.txt"
in_filepath = pathlib.Path(path_root, in_filename)
print(in_filepath)
input_text = str(load_text(in_filepath))
# for i in range(0, 20):
#     print(input_text[i])

### Output Text
out_text = ""


### Last Solution
""" 
inputlist = input_text.split(".")
newlist = []
for line in inputlist:
    correctline = line.split(" ")
    correctline.reverse()
    newlist.append(" ".join(correctline))

out_text = ".".join(newlist)

"""
inputlist = input_text.split(" ")
newlist = []
secondlist = []

for word in inputlist:
    letterlist = list(word)
    letterlist.reverse()
    newword = "".join(letterlist)
    newlist.append(newword)

out_text = " ".join(newlist)
#print(out_text)
print(out_text[:100])

### Dump text to file
#out_filename = "decoded-3.txt"
#write_text(out_filename, out_text)