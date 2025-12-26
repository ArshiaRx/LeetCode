class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Create a Roman-to-Integer Mapping (Dictionary) - maps each roman character to its correxpondi9ng integer value
        roman_map = { 
                    'I': 1,     'V': 5,     'X': 10,
                    'L': 50,    'C': 100,   
                    'D': 500,   'M': 1000
                    }        

        # Initialize two variables
        result = 0
        prev = 0

        # Loop through the string
        for char in reversed(s):
            
            # set the value to its corresponding int value. Ex: if char is 'L' is set value to '50'.
            value = roman_map[char]

            if value < prev:
                result -= value

            else:
                result += value
            prev = value
            
        return result    