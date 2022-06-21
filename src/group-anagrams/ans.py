class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # alphabetize strings
        # keep list of "keys" we have seen

        keys = {}
        anagrams = []

        for word in strs:
            key = ''.join(sorted(word))  # alphabetically sorted version of word
            if keys.get(key) is None:
                keys[key] = len(keys)
                anagrams.append([word])
            else:
                i = keys.get(key)
                anagrams[i].append(word)

        return anagrams
