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
in_filename = "puzzle-4.txt"
in_filepath = pathlib.Path(path_root, in_filename)
print(in_filepath)
input_text = str(load_text(in_filepath))
# for i in range(0, 20):
#     print(input_text[i])

### Output Text
out_text = ""


### Last Solution
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

"""

#input_text = r"z ytimiDxt nagebqrednu ozw dnatsq sa ,yhxord ehtjuoy ypoz nam gnxlot dahx ,reh djoep wefqrew elpq elba exneve otzni teg side."
#input_text = r"""n ytimiDq dekoolsc niagavlluferaeve ta ywmoc yrek tnenopw eht foqlebroodwlzzup lw ehT .eisnottubjesmeht aew sevldfinu erjb ylmroga ;knaly ehs llhof wenkkatrec rj saw nimht tahtjrew erenthgie eleht fo l ehT .mg euqalpkis diasvot ylpmp emoc" c -- "niieht tubww rood bkcol saehgit de f sA .tolnO" rogifsim yfdeen stp"ylppa leW ... tahw ,llda saw tutifsim x tahW ?wid erehrif t'ndt?"""
#input_text = r"hzag reHhtfird epnwod dezeht ot xm rood at."
#input_text = """WE MMERRY GREET
#WHOO CCLLEANNS THEIIR FEEETT"""

output = ""
char_count = 0
buffer = ""

for c in input_text:
    buffer += c
    char_count += 1
    if (char_count == 8):
        output += buffer[2]
        output += buffer[1]
        output += buffer[0]
        output += buffer[6]
        output += buffer[5]
        output += buffer[4]
        buffer = ""
        char_count = 0

output += buffer

#print(output[:100])

#import math
#for i in range(len(input_text) / 8):
#    for j in range(8):
#        print(input_text[8 * i:8 * i + j])


#print(out_text)
#print(out_text[:100])

### Dump text to file
out_filename = r"DimityJones\solution-4.txt"
write_text(out_filename, output)