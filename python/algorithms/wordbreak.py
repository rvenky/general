

def wordBreak (strBuf, legalWordsSet):
    """
     Break a long sequence of characters into legal words with spaces
    """
    for index in xrange(len(strBuf) + 1):
        prefix = strBuf[:index]  # can optimize this if 
        if prefix in legalWordsSet:
            rest = strBuf[index:]
            if rest == "":
                yield prefix
            else:
                words = wordBreak (rest, legalWordsSet)
                for sentence in words:
                    yield prefix + ' ' + sentence
                
def test_wordBreak():
    legalWordsSet = set (['i', 'love', 'is', 'ice', 'cream', 'icecream', 'every', 'day',
                          'from', 'costco', 'once', 'a', 'year', 'nice', 'everyday'])
    
    assert list (wordBreak ('costco', legalWordsSet)) == ['costco']
    
    assert list (wordBreak ('everydayisaniceday', legalWordsSet)) == ['every day is a nice day', 'everyday is a nice day']
    
    assert list (wordBreak ('everydayonceayear',legalWordsSet)) ==  [ 'every day once a year', 'everyday once a year']
    
    #print list (wordBreak ('everydayiloveicecream',legalWordsSet))
    assert set (wordBreak ('everydayiloveicecream',legalWordsSet)) ==set ( [ 'every day i love ice cream',
                                                                         'every day i love icecream', 
                                                                         'everyday i love ice cream',
                                                                         'everyday i love icecream'])
    assert list (wordBreak ('iloveicecream',legalWordsSet))  == [ 'i love ice cream', 'i love icecream']

