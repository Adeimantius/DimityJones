
class Decoder:
    def solve(self, encoded_puzzle_text):
        out_text = ""
        inputlist = encoded_puzzle_text.split(".")
        newlist = []
        for line in inputlist:
            correctline = line.split(" ")
            correctline.reverse()
            newlist.append(" ".join(correctline))

        out_text = ".".join(newlist)
        return out_text