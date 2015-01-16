

def numberOfPaths (X, Y):
    """
    Path from 0,0 to x,y either going right or down by unit distance
    """
    def recur (x, y):
        if x==X or y==Y:
            return 1
        else:
            return recur (x+1, y) + recur (x, y+1)
        
    recur (0,0)
    
def test_numberOfPaths ():
    assert numberOfPaths (1,1) == 2
        
    