class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        cleaned_text = ''.join(char for char in s if char.isalnum())
        chars = list(cleaned_text)
        result = [char.lower() for char in chars]
        n = len(result)
        left = 0
        right = n - 1
        

        print(f"chars list {chars}")
        while left < right:
            if result[left] != result[right]:
                return False
            left += 1
            right -= 1
            
        return True
