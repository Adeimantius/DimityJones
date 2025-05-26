

class Decoder:
    def solve(self, encoded_puzzle_text):
        out_text = ""
        char_count = 0
        buffer = ""

        for c in encoded_puzzle_text:
            buffer += c
            char_count += 1
            if (char_count == 9):
                out_text += buffer[6]
                out_text += buffer[5]
                out_text += buffer[7]
                out_text += buffer[2]
                out_text += buffer[1]
                out_text += buffer[0]
                out_text += buffer[8]
                out_text += buffer[4]
                out_text += buffer[3]                
                buffer = ""
                char_count = 0

        out_text += buffer
        return out_text