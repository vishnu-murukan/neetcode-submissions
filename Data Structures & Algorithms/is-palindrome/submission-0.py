class Solution:
    def isPalindrome(self, s: str) -> bool:
        b= False
        new = ""
        for i in s:
            if i.isalnum():
                new += i.lower()
         
        if new == new[::-1]:
            b = True
        else:
            b=False

        return b
        
        
        