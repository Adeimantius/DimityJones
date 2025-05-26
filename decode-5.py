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
in_filename = "puzzle-5.txt"
in_filepath = pathlib.Path(path_root, in_filename)
print(in_filepath)
input_text = str(load_text(in_filepath))
# for i in range(0, 20):
#     print(input_text[i])

### Output Text
out_text = ""


### Last Solution
""" 
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

"""

#input_text = 

#print(out_text)
#print(out_text[:100])

### Dump text to file
out_filename = r"DimityJones\solution-5.txt"
write_text(out_filename, out_text)