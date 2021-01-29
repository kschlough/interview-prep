class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # turn into a string
        str_dig = ""
        for digit in digits:
            digit = str(digit)
            str_dig += digit
            
        # turn into int to increment
        incremented = (int(str_dig) + 1)
        
        # blank return list
        return_list = []
        
        # catch if it's any # of 0s
        if sum(digits) == 0:
            for i in range(len(digits)-1):
                return_list.append(0)
            return_list.append(1)
        
        else:
        # turn back into string to increment
            for i in str(incremented):
                return_list.append(int(i))
            
        return return_list