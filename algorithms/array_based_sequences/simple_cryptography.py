class CeasarCipher:
    def __init__(self, rotation):
        self.rotation = rotation
        self.alphabet_int_codes = []
        self.replacements = []

    def _make_alphabet(self):
        first = ord("A")
        last = ord("Z")
        while first < last:
            self.alphabet_int_codes.append(first)
            first += 1
        self.alphabet_int_codes.append(last)

    def _make_replacements(self):
        return [
            self.alphabet_int_codes[(i + self.rotation) % len(self.alphabet_int_codes)]
            for i in range(len(self.alphabet_int_codes))
        ]

    def transform(self, secret):
        cipher = []
        for c in secret:
            if c.isalpha():
                cipher.append(self.replacements[self.alphabet_int_codes.index(ord(c))])
        return ""


if __name__ == "__main__":
    cc = CeasarCipher(3)
    cc.transform("THE EAGLE IS IN PLAY; MEET AT JOE'S")
