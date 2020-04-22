class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x: x[0])
        
        #print(intervals)
        
        merged = []
        
        for interval in intervals:
            #Checking to see if the item is in merged.. or if the last item index              #1 in in merged is less than the current index 0 
             # If so then append to the merged function
            if not merged or merged [-1][1] < interval[0]:
                merged.append(interval)
            else: 
                #change last index1 to the maximum of the last index 1 and current                  #index1
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged