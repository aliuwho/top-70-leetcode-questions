class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        paren = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        match = ""
        for c in s:
            if c in paren.keys():
                match += paren[c]
            else:
                if len(match) == 0 or match[-1] != c:
                    return False
                match = match[:-1]
        return len(match) == 0
