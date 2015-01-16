

'''
Problem:
Generate a new array from an array of numbers. 
Start from the beginning. Put the number of occurrences of some number first, 
and then that number.
For example, from array: 1, 1, 2, 3, 3, 1
You should get: 3 1, 1 2, 2 3
'''

'''
Solution:
  Iterate the input array
  Keep frequency of array_entries in a hash map
  Keep order of uniq entries (only if we want result in input array order)
  
  Iterate map to get key, count in order of keys in uniq entries
  
  Note: Best we can do is O(n) since we need to examine every entry in input array
  
  Testing: shell> py.test frequency.py

'''

def frequency_count (integers):
    
    if integers == None:
        return None
    result = []
    uniqs = []            # Contains unique values from input array
    int_count = dict()    # Map to keep count of each value in array
    for num in integers:
        if num in int_count:
            int_count [num] += 1
        else:
            int_count[num] = 1
            uniqs.append (num)
            
    for num in uniqs:
        val = str(int_count[num])  + " " + str (num)
        result.append ( val)
        
    return result

def test_frequency_count ():
    assert frequency_count ([]) == []
    assert frequency_count(None) == None
    assert frequency_count ([1, 1, 2, 3, 3, 1]) == ["3 1","1 2","2 3"]
    assert frequency_count ([7]) == ["1 7"] 
    assert frequency_count ([7,7]) == ["2 7"]
            
            
    
    



