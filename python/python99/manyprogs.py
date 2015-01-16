


list1=[1,2,3,4,5]

list2 = ['a','b','c','d','e']


def removeDups1 (list):
    ret = []
    prev = None
    for item in list:
        if item != prev:
            ret.append (item)
            prev = item
    return ret



def test_dups1_1 ():
    list = [1,2,3,4,5]
    assert (removeDups1(list) == list)


def test_dups1_2 ():
    list = [2,2,3,3,4,4,5,5,5]
    assert (removeDups1(list) == [2,3,4,5])


def last (list):
    return list [-1]


def test_last ():
    assert (last (list1) == 5)
    assert (last (list2) == 'e')


def penultimate (list):
    return list [-2]


def reverse (list):
    return list[len(list):-len(list) - 1:-1]


def test_reverse ():
    assert (reverse(list1) == [5,4,3,2,1])
    assert (reverse(list2) == ['e','d','c','b','a'])


def even_indices (list):
    return list[::2]

def test_even_indices ():
    assert (even_indices(list1) == [1,3,5])


nested_list1 = [0,1,[2,3],4,5,[6,7,8]]
nested_list2 = [0,1,[2,3],4,5,[6,7,8,[9,10]]]

""" 
    Recursive way to flatten a list

"""

def flatten(nestedList):

    def recurse (alist):
        print "here " + str (alist)
        for item in alist:
            print item
            if isinstance(item,list):
                print "there " + str(item)
                for item in recurse (item):
                    yield item

            else:
                yield item
    return list (recurse(nestedList))


def test_flatten ():
    assert (flatten(list1) == list1)
    assert (flatten (nested_list1)== [0,1,2,3,4,5,6,7,8])
    assert (flatten (nested_list2)== [0,1,2,3,4,5,6,7,8,9,10])


def test_flatten_non_recur ():
    assert (1 == 2, "TODO implement flatten no-recursive")


dups_list1 = [1,1,1,2,2,2,3,3,4,5]

from itertools import groupby
def remove_dups (alist):
    return [key for key, group in groupby(alist)]


def test_remove_dups ():
    assert (remove_dups (dups_list1)== [1,2,3,4,5])

def sublists_duplicates(alist):
    return [list(group) for key, group in groupby(alist)]


def test_sublists_duplicates():
    assert (sublists_duplicates(dups_list1) == [ [1,1,1], [2,2,2], [3,3],[4],[5]])


"""
Problem 10: Run-length encoding of a list

"""

def runLength (alist):
    return [ (key,len(list(group))) for key,group in groupby (alist)]


def test_runLength ():
    assert ( runLength (dups_list1) == [(1,3), (2,3), (3,2), (4,1), (5,1)])


def decode_rle1 (alist):

    def iter (alist):
        for (key,count) in alist:
            for i in xrange(count):
                yield key

    return list (iter(alist))


def test_decode_rle1 ():
     assert (dups_list1 == decode_rle1 (runLength(dups_list1))) 

def runLength2 (alist):
    def element (key, grp):
        length = len(list(grp))
        return key if length == 1 else (key, length)

    return [ element (key, group) for key,group in groupby (alist)]

def test_runLength2 ():
    assert (runLength2 (dups_list1) == [(1,3), (2,3), (3,2), 4, 5])



def decode_rle2(alist):
    def iter(alist):
        for item in alist:
            if isinstance (item, tuple):
                key, count = item
                for i in xrange(count):
                    yield key
            else:
                yield item

    return list (iter(alist))


def test_decode_rle2 ():
    assert (dups_list1 == decode_rle2 (runLength2(dups_list1)))

def dup_list (alist):
    return [item for item in alist for i in xrange(2)]


def test_dup_list ():
    assert ( dup_list (list1) == [1,1,2,2,3,3,4,4,5,5])


def dup_list_n (alist, n):
    return [item for item in alist for i in xrange(n)]


def test_dup_list_n ():
    assert ( dup_list_n (list1, 2) == [1,1,2,2,3,3,4,4,5,5])
    assert ( dup_list_n (list1, 3) == [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5])

def drop_every_n (alist, n):
    return [ item for i,item in enumerate(alist) if (i +1) % n != 0]

def test_drop_every_n ():
    assert ( drop_every_n (list1, 1) == [])
    assert ( drop_every_n (list1, 2) == [1,3,5])
    assert ( drop_every_n (list1, 3) == [1,2,4,5])

def split_at_n (alist, n):
    return alist[:n], alist[n:]

def test_split_at_n ():
    assert( split_at_n (list1,1) == ([1], [2,3,4,5]))
    assert( split_at_n (list1,2) == ([1,2], [3,4,5]))


def permute (str):
    if len (str) == 1:
        return [str]
    else:
        item = str[0]
        tail = str[1:]

        

    


