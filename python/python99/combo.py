
"""
  Generate all combinations of elements 
   n C r   
   no duplicates

   uses formula

   nCr = nCr-1 + n-1Cr-1
"""
def combo ( list1, r):
    if len(list1) == r:
        yield list1

    elif r == 1:
        for elem in list1:
            yield [elem]
    else:
        tail = list1[1:]
        for item in combo (tail, r):
            yield item

        head = list1[0]
        list_head = [head]
        for item in combo (tail, r -1):
            yield list_head + item

"""
  Permutations 
  nPr =  r * n-1Pr-1 + n-1Pr 
"""
def permute (list1, r):
    if r==1:
        for item in list1:
            yield [item]
    elif r > len(list1):
        pass

    else:
        tail = list1[1:]
        for litem in permute (tail, r):
            yield litem
        head = list1[0]
        lhead = [head]
        for litem in permute (tail, r -1):
            for i in xrange (len(litem),-1,-1):
                yield litem [:i] + lhead + litem [i:] 



    

for item in combo ([1,2,3,4,5,6,7,8,9], 8):
    print item

for item in permute ([1,2,3, 4], 2):
    print item

for item in permute (list ("anywkrlflok"), 5):
    print item
