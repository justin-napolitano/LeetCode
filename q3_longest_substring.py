class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_list = []
        max_length = 0
    
        for x in s:
            if x in str_list:
                str_list = str_list[str_list.index(x)+1:]
            
            str_list.append(x)    
            max_length = max(max_length, len(str_list))
        
        return max_length
  

"""
        maximum = 0
        counter = 0
        last = None
        seen = []
        for iterator, character in enumerate(s):
            if character == last and character in seen: 
                counter = 1
                last = character
                seen = []
                seen.append(character)
            elif character in seen:
                counter = 1 
                last = character
                seen = []
                seen.append(character)
            else:
                counter = counter + 1
                last = character
                seen.append(character)
                if maximum < counter:
                    maximum = counter
                
        return maximum
                
            
 """           
            