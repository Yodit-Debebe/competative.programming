class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        stack = []
        visited = set()               
        for char in s:      
            char_count[char] -= 1          
            if char in visited:
                continue                        
            while stack and stack[-1] > char and char_count[stack[-1]] > 0:
                visited.remove(stack.pop())          
            stack.append(char)
            visited.add(char)
        return ''.join(stack)
