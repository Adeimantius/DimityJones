import os
import sha_test

def get_files_in_directory(relative_path="."):
    try:
        absolute_path = os.path.join(os.getcwd(), relative_path)
        items = os.listdir(absolute_path)
        files = [os.path.join(absolute_path, item) for item in items if os.path.isfile(os.path.join(absolute_path, item))]
        return files
    except FileNotFoundError:
        print(f"Directory not found")
        return []
    
def generate_filename_list_for_directory(directory, filename_format, range_max, suffix = ".txt"):
    try:
        absolute_path = os.path.join(os.getcwd(), directory)
        files = []
        for i in range(0, range_max):
            files.append(os.path.join(absolute_path, filename_format + str(i) + suffix))
        return files
    except FileNotFoundError:
        print(f"Directory not found")
        return []
    
def load_text(filename):
    with open(filename, "r") as f:
        return f.read()

def write_text(filename, text):
    with open(filename, "w") as f:
        f.write(text)
        return True
    
def trim_on_chapter_marker(input, marker="#####"):
    index = input.find(marker)
    if index != -1:
        return input[index+len(marker):]
    return input

def compare_solution_to_hash(decoded_text, expected_hash, index):
    sha_match = sha_test.compare_sha256_hashes(decoded_text, expected_hash)
    result_text_intro = "EVALUATING PUZZLE #" + str(index) + " SOLUTION OUTPUT... "
    if sha_match:
        print(result_text_intro + "MATCH! SOLUTION WAS CORRECT!")
        return True
    else:
        print(result_text_intro + "MISMATCH! SOLUTION WAS NOT CORRECT!")
        return False