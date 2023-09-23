class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # Use two dictionaries to store the values from the lists. 
        dict1, dict2 = {}, {}
        res_sum = len(list1)+len(list2) # Will be used to store the sum of indices
        
        # Copy the elements from the list into a dictionary as keys, and indices as values
        for index, value in enumerate(list1):
            dict1[value] = index
        
        # Loop through list2, and check if the elements exist 
        for index, value in enumerate(list2):
            if value in dict1:
                tmp_sum = dict1[value] + index
                dict2[tmp_sum] = dict2.get(tmp_sum, []) + [value]
                res_sum = min(tmp_sum, res_sum)
        return dict2[res_sum]