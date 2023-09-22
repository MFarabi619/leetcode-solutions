class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # We iterate through both strings at the same time, and use a hash map. The letter from string 's' is the key, and the letter from string 't' is the value. If a key-value pair doesn't exist, we add it. If a key exists, then we check if the current value equals what is already stored in the hash map. If not, then we fail the case.
        
        hashMap = {}
        mappedChars = set()  # to keep track of chars in 't' that have been mapped
        
        # We can use the zip function to iterate over both strings at the same time.
        for char1, char2 in zip(s, t):
            if char1 in hashMap:
                if hashMap[char1] != char2:
                    return False
            else:
                # Check if char2 has been mapped to some other character in 's'
                if char2 in mappedChars:
                    return False
                hashMap[char1] = char2
                mappedChars.add(char2)
        
        return True
        