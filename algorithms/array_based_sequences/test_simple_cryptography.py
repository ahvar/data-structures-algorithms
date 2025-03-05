import unittest
from .simple_cryptography import CeasarCipher


class TestSimpleCryptography(unittest.TestCase):

    def setUp(self):
        self.cc = CeasarCipher(3)
        self.cc._make_alphabet()
        self.cc._make_replacements()
        self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.replacements = list("DEFGHIJKLMNOPQRSTUVWXYZABC")

    def test_replacement(self):

        for i in range(len(self.alphabet)):
            assert chr(self.cc.alphabet_int_codes[i]) == self.alphabet[i]

        for i in range(len(self.replacements)):
            assert chr(self.cc.replacements[i]) == self.replacements[i]

    def test_transform(self):
        self.cc.transform("THE EAGLE IS IN PLAY; MEET AT JOE'S")
