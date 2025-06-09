"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations
that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that
1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

"""
from typing import List
class Solution:
    def _add_letters(self, letters, chars):
        if not letters: return [str(char) for char in chars]
        combo_map = {}
        updated = []
        for j in range(len(chars)):
            char = chars[j]
            char_combos = [letter + char for letter in letters]
            combo_map[char] = char_combos
        for char_key,combo_list in combo_map.items():
            for string in combo_list:
                updated.append(string)
        return updated

    def letterCombinations(self, digits: str) -> List[str]:
        all = {2: 'abc',3: 'def',4: 'ghi',5: 'jkl',6: 'mno',7: 'pqrs',8: 'tuv',9: 'wxyz'}
        letters = []
        for digit in digits:
            if 2 <= int(digit) <= 9:
                chars = all.get(int(digit))
                new = self._add_letters(letters, chars)
                letters = new
        return letters

        
if __name__ == "__main__":
    digits = '23'
    solution = Solution()
    print(solution.letterCombinations(digits))
