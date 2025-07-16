class Solution:
    def isValid(self, word: str) -> bool:
        has_v = False
        has_a = False

        import string
        lword = word.lower()
        if len(word) < 3: 
            return False
        for i in list(lword): 
            if i in list(string.ascii_lowercase):
                if i in 'aeiou':
                    has_v = True
                else:
                    has_a = True
            else:
                if i not in [str(x) for x in range(10)]:
                    return False
        return has_v and has_a

