import os
import puzzle_utility_lib as plib
import decoder
import sha_test

solutions_scripts_dirname = "solutions-scripts"
solutions_text_dirname = "solutions-text"

sha_list_file = os.path.join(os.getcwd(), "sha_list.txt")
solutions_text_path = os.path.join(os.getcwd(), solutions_text_dirname)
numbered_sha_list = plib.load_text(sha_list_file).splitlines()
sha_list = [line[4:] for line in numbered_sha_list]
    
solutions_scripts_files = plib.get_files_in_directory(solutions_scripts_dirname)
solutions_text_files = plib.generate_filename_list_for_directory(solutions_text_dirname, "solution-", 89)

print("""\
                             -|             |-
         -|                  [-_-_-_-_-_-_-_-]                  |-
         [-_-_-_-_-]          |             |          [-_-_-_-_-]
          | o   o |           [  0   0   0  ]           | o   o |
           |     |    -|       |           |       |-    |     |
           |     |_-___-___-___-|         |-___-___-___-_|     |
           |  o  ]              [    0    ]              [  o  |
           |     ]   o   o   o  [ _______ ]  o   o   o   [     | ----__________
_____----- |     ]              [ ||||||| ]              [     |
           |     ]              [ ||||||| ]              [     |
       _-_-|_____]--------------[_|||||||_]--------------[_____|-_-_
      ( (__________------------_____________-------------_________) )

                        Dimity Jones in Puzzle Castle: 
            An Electronic Escape Novel in Eighty-Nine Ciphertexts
      
""")
print("Running decoding solutions.")

for i in range(0, len(solutions_scripts_files) - 1):
    decoded_text_file = solutions_text_files[i]
    decoded_text = plib.load_text(decoded_text_file)
    if not plib.compare_solution_to_hash(decoded_text, sha_list[i], i):
        break
    decoder_script_file = solutions_scripts_files[i+1]
    next_solution_file = os.path.join(solutions_text_path, "solution-" + str(i+1) + ".txt")
    encoded_text = plib.trim_on_chapter_marker(decoded_text)
    next_decoded_text = decoder.decode_chapter_to_output_file(encoded_text, decoder_script_file, next_solution_file)

# Finally, the last solution that has been finished
final_index = len(solutions_scripts_files) - 1
decoded_text_file = solutions_text_files[final_index]
decoded_text = plib.load_text(decoded_text_file)
plib.compare_solution_to_hash(decoded_text, sha_list[final_index], final_index)


