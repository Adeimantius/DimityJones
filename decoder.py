import importlib.util
import puzzle_utility_lib as plib

""" 
Have each decoder implement Decoder class with a solve method like so: 
"""
# class Decoder:
#     def solve(encoded_puzzle_text):
#         return encoded_puzzle_text

def decode_chapter(encoded_text, decode_function_file):
    spec = importlib.util.spec_from_file_location("Decoder", decode_function_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    decoder = module.Decoder()
    return decoder.solve(encoded_text)
    
def decode_chapter_to_output_file(encoded_text, decode_function_file, output_file):
    plib.write_text(output_file, decode_chapter(encoded_text, decode_function_file))
