class Decoder:
    def solve(self, encoded_puzzle_text):
        numchars = len(encoded_puzzle_text)
        outtext = ""
        fwd = 0
        bck = numchars - 1
        next = fwd
        for i in range(0, numchars):
            outtext += encoded_puzzle_text[next]
            if i % 2 == 0:
                fwd += 1
                next = bck
            else:
                bck -= 1
                next = fwd
        return outtext