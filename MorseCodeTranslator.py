class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        transformation_words = []
        difference = 0
        alphabetToMorse = {
            'a': '.-',
            'b': '-...',
            'c': '-.-.',
            'd': '-..',
            'e': '.',
            'f': '..-.',
            'g': '--.',
            'h': '....',
            'i': '..',
            'j': '.---',
            'k': '-.-',
            'l': '.-..',
            'm': '--',
            'n': '-.',
            'o': '---',
            'p': '.--.',
            'q': '--.-',
            'r': '.-.',
            's': '...',
            't': '-',
            'u': '..-',
            'v': '...-',
            'w': '.--',
            'x': '-..-',
            'y': '-.--',
            'z': '--..'}
        for i in words:
            temp_str = ''
            for y in i:
                temp_str += alphabetToMorse[y]
            if temp_str not in transformation_words:
                difference += 1
            transformation_words.append(temp_str)
        return difference


si = Solution()
sol = si.uniqueMorseRepresentations(["gin","zen","gig","msg"])
print(sol)
