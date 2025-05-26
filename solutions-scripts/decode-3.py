
class Decoder:
    def solve(self, encoded_puzzle_text):
        inputlist = encoded_puzzle_text.split(" ")
        newlist = []
        secondlist = []

        for word in inputlist:
            letterlist = list(word)
            letterlist.reverse()
            newword = "".join(letterlist)
            newlist.append(newword)

        out_text = " ".join(newlist)

        return out_text