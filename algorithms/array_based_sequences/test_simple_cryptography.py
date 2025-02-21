import unittest
from simple_cryptography import make_rule, make_alphabet


class TestSimpleCryptography(unittest.TestCase):

    def setUp(self):
        self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.replacements = list("DEFGHIJKLMNOPQRSTUVWXYZABC")

    def test_replacement(self):
        alphabet_int_codes = make_alphabet()
        for i in range(len(self.alphabet)):
            assert chr(alphabet_int_codes[i]) == self.alphabet[i]
        replacements = make_rule(alphabet_int_codes, 3)
        for i in range(len(self.replacements)):
            assert chr(replacements[i]) == self.replacements[i]
