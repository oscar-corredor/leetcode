from collections import OrderedDict

class Solution(object):
    def __init__(self):
        # self.valid_characters = '(':1, ")":2, '[':3,']':4, '{':5, '}':6}
        self.valid_characters = OrderedDict((("(", True), (")", False),("[", True), ("]", False),("{", True), ("}", False)))        

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # check if the number of characters is even
        if(len(s)%2 != 0):
            return False        
        # check the string element by element
        previous = -1
        # indicated whether a parenthesis has been opened
        opened = False
        for c in s:
            # check that it's a valid element
            if c not in self.valid_characters:
                return False
            else:
                # opened = self.valid_characters[c]
                if not self.valid_characters[c] and not opened:
                    return False
                elif previous == -1:
                    previous = self.valid_characters.keys().index(c)
                    opened = self.valid_characters.keys().index(c)
                else:
                    if not self.valid_characters[c] and self.valid_characters.keys().index(c) - previous != 1:
                        return False
                    else:
                        previous = self.valid_characters.keys().index(c)
                        opened = self.valid_characters[c]
        return True

print(Solution().isValid('()[]{}'))
