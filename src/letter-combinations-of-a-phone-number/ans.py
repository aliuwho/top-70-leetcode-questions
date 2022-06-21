class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if len(digits) == 0:
            return []

        letters = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        combs = []
        for digit in digits:
            trans = letters[digit]
            if len(combs) == 0:
                for letter in trans:
                    combs.append(letter)
            else:
                nextCombs = []
                for comb in combs:
                    for letter in trans:
                        nextCombs.append(comb + letter)
                combs = nextCombs

        return combs
