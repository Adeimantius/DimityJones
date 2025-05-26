
class Decoder:
    def solve(self, encoded_puzzle_text):
        output = ""
        char_count = 0
        buffer = ""

        for c in encoded_puzzle_text:
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
        return output