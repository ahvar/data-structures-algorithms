"""
"""


class CeasarCipher:
    def __init__(self, rotation):
        self._rotation = rotation
        self._alphabet_int_codes = []
        self._replacements = []

    def _make_alphabet(self):
        first = ord("A")
        last = ord("Z")
        while first <= last:
            self._alphabet_int_codes.append(first)
            first += 1

    def _make_replacements(self):
        self._replacements = [
            self._alphabet_int_codes[
                (i + self._rotation) % len(self._alphabet_int_codes)
            ]
            for i in range(len(self._alphabet_int_codes))
        ]

    def transform(self, secret):
        """
        1. Convert each character in the secret string to its ordinal value
        2. Get the index of that value from the list of alphabet integer codes
        3. Use that index to find the code of the replacement character

        """
        cipher = []
        for c in secret:
            if c.isalpha():
                cipher.append(
                    chr(self._replacements[self._alphabet_int_codes.index(ord(c))])
                )
            else:
                cipher.append(c)
        print(cipher)
        return cipher

    @property
    def alphabet_int_codes(self):
        return self._alphabet_int_codes

    @property
    def replacements(self):
        return self._replacements

    @property
    def rotation(self):
        return self._rotation


if __name__ == "__main__":
    cc = CeasarCipher(3)
    cc._make_alphabet()
    cc._make_replacements()
    cc.transform("THE EAGLE IS IN PLAY; MEET AT JOE'S")
