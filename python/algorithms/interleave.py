

def interleave (s1, s2):
    """
    Interleave 2 strings
    if s1 is empty s2
    else if s2 empty s1
    characters in the result appear in order they appear in s1 and s2
    
    """
    
    if not s1:
        yield s2 
    elif not s2:
        yield s1
    else:
        for str3 in interleave (s1[1:],s2 ):
            yield s1[0] + str3
        for str4 in interleave (s1, s2[1:]):
            yield s2[0] + str4
            
def isInterleaved (s1, s2, s1s2):
    if not s1:
        return s2 == s1s2
    elif not s2:
        return s1 == s1s2
    elif len(s1s2) != len(s1) + len(s2):
        return False
    else:
        return (s1[0] == s1s2[0] and isInterleaved (s1[1:], s2, s1s2[1:])) or (s2[0] == s1s2[0] and isInterleaved(s1, s2[1:], s1s2[1:]))
            
def test_interleave ():
    assert list (interleave("", "abc") )== ["abc"]
    assert list(interleave("xyz", "")) == ["xyz"]
    assert list(interleave("x", "a")) == ["xa", "ax"]
    
    assert set (list(interleave("ab", "x"))) == set (["abx", "xab", "axb"])
    
    assert set (list(interleave("ab", "xy"))) == set (["abxy", "axby", "axyb", "xyab", "xayb", 
                                                       "xaby"])
    
def test_isInterleaved ():
    
    assert isInterleaved ("a", "b", "ab")
    assert not isInterleaved ("a", "b", "abc")
    assert isInterleaved ("a", "b", "ba")
    assert isInterleaved ("a", "b", "ba")
    assert isInterleaved ("a", "bc", "abc")
    assert isInterleaved ("a", "bc", "bca")
    assert isInterleaved ("a", "bc", "bac")
    assert isInterleaved ("a", "bc", "bac")
    assert isInterleaved ("ax", "ay", "axay")
    assert isInterleaved ("ax", "ay", "aaxy")
    assert isInterleaved ("ax", "ay", "aayx")
    assert isInterleaved ("ax", "ay", "ayax")
    assert not isInterleaved ("ax", "ay", "ayxa")


