# a4test.py
# LYLLA YOUNES, ley23
# DATE COMPLETED HERE
""" Unit Test for Assignment A4"""
import cornelltest
import a4

# NEW ASSERT to help with testing

def assert_lists_equal(expected, received):
    """Helper function to verify that expected == received
    
    Because of how lists work, we cannot say
    
       cornelltest.assert_equals(expected, received)
    
    The lists are different folders and the contents may be in a 
    different order. So instead, we break this down into several 
    tests, which we put here.
    
    As always, we put the value that we expect on the  left, and the 
    value being tested on the right (in parameter received).
    
    Precondition: expected is a list"""
    # Check received is a list of the right length
    if list != type(received):
        msg = 'assert_lists_equal: '+`received`+' is not a list'
        cornelltest.quit_with_error(msg)
    
    if len(expected) != len(received):
        msg = ('assert_lists_equal: '+`received`+' does not have expected length'
                +`len(expected)`)
        cornelltest.quit_with_error(msg)
    
    # Check each of the contents of expected
    for item in expected:
        if not item in received:
            msg = 'assert_lists_equal: '+`received`+' is missing element '+`item`
            cornelltest.quit_with_error(msg)
    


# Test Procedures

def test_build_word_list():
    """Test function build_word_list"""
    print 'Testing build_word_list'
    words = a4.build_word_list('short.txt')
    expected = ['the', 'be','to','of','and','a','in','that','have','it']
    assert_lists_equal(expected, words)
    
    print 'build_word_list is working correctly'


def test_word_list_by_size():
    """Test function word_list_by_size"""
    print 'Testing word_list_by_size'
    # Make the word list
    words = ['the', 'be','to','of','and','a','in','that','have','it']
    
    # Call the function
    other = a4.word_list_by_size(words, 2)
    
    # Compare to what we expect
    expected = ['be','to','of','in','it']
    assert_lists_equal(expected, other)
    
    print 'word_list_by_size is working correctly'


def test_word_list_extend():
    """Test function word_list_extend"""
    print 'Testing word_list_extend'
    # Create a short word list
    words = ['o', 'at', 'ong']
    
    # Call the function
    other = a4.word_list_extend(words, 's')
    
    # Compare to what we expect
    expected = ['so','sat','song']
    assert_lists_equal(expected, other)
    
    # Verify that we DID NOT change words
    assert_lists_equal(['o', 'at', 'ong'], words)

    # Do this one more time with a prefix that is more than one letter
    other = a4.word_list_extend(words, 'pr')
    
    # Verify that we loaded the right number of words
    expected = ['pro','prat','prong']
    assert_lists_equal(expected, other)
    
    print 'word_list_extend is working correctly'


def test_pmap_add_word():
    """Test function pmap_add_word"""
    print 'Testing pmap_add_word'
    
    # Start with an empty prefix map
    pmap = {}
    a4.pmap_add_word(pmap,'a')
    
    # Verify that pmap now has two keys (space and 'a')
    # Note use of helper to make this test easier to read
    cornelltest.assert_equals(2, len(pmap))
    cornelltest.assert_true('' in pmap)
    assert_lists_equal(['a'], pmap[''])
    cornelltest.assert_true('a' in pmap)
    assert_lists_equal([''], pmap['a'])
    
    # Add something with two letters
    a4.pmap_add_word(pmap,'by')
    
    # Verify the keys again
    cornelltest.assert_equals(4, len(pmap))
    cornelltest.assert_true('' in pmap)
    assert_lists_equal(['a','b'], pmap[''])
    cornelltest.assert_true('a' in pmap)
    assert_lists_equal([''], pmap['a'])
    cornelltest.assert_true('b' in pmap)
    assert_lists_equal(['y'], pmap['b'])
    cornelltest.assert_true('by' in pmap)
    assert_lists_equal([''], pmap['by'])
    
    # One last time with overlap
    a4.pmap_add_word(pmap,'at')
    
    # Verify the keys again
    cornelltest.assert_equals(5, len(pmap))
    cornelltest.assert_true('' in pmap)
    assert_lists_equal(['a','b'], pmap[''])
    cornelltest.assert_true('a' in pmap)
    assert_lists_equal(['','t'], pmap['a'])
    cornelltest.assert_true('at' in pmap)
    assert_lists_equal([''], pmap['at'])
    cornelltest.assert_true('b' in pmap)
    assert_lists_equal(['y'], pmap['b'])
    cornelltest.assert_true('by' in pmap)
    assert_lists_equal([''], pmap['by'])
    
    print 'pmap_add_word is working correctly'

def test_word_list_to_pmap():
    """Test function word_list_to_pmap"""
    print 'Testing function word_list_to_pmap'
    
    # Start with an empty word list
    words = []
    pmap = a4.word_list_to_pmap(words)
    
    # Should be empty dictionary
    cornelltest.assert_equals(dict, type(pmap))
    cornelltest.assert_equals(0, len(pmap))
    
    # One word, two letters
    words = ['at']
    pmap = a4.word_list_to_pmap(words)
    
    # Similar test format to pmap_add_word
    cornelltest.assert_equals(3, len(pmap))
    assert_lists_equal(['a'], pmap[''])
    cornelltest.assert_true('a' in pmap)
    assert_lists_equal(['t'], pmap['a'])
    cornelltest.assert_true('at' in pmap)
    assert_lists_equal([''], pmap['at'])
    
    # Several words
    words = ['at', 'by', 'a']
    pmap = a4.word_list_to_pmap(words)
    
    # Similar test format to pmap_add_word
    cornelltest.assert_equals(5, len(pmap))
    cornelltest.assert_true('' in pmap)
    assert_lists_equal(['a','b'], pmap[''])
    cornelltest.assert_true('a' in pmap)
    assert_lists_equal(['','t'], pmap['a'])
    cornelltest.assert_true('at' in pmap)
    assert_lists_equal([''], pmap['at'])
    cornelltest.assert_true('b' in pmap)
    assert_lists_equal(['y'], pmap['b'])
    cornelltest.assert_true('by' in pmap)
    assert_lists_equal([''], pmap['by'])
    
    print 'word_list_to_pmap is working correctly'


def test_pmap_to_word_list():
    """Test function pmap_to_word_list"""
    print 'Testing function pmap_to_word_list'
    
    # Start with an empty prefix map
    pmap = {}
    words = a4.pmap_to_word_list(pmap)
    
    # Should be empty list
    cornelltest.assert_equals(list, type(words))
    cornelltest.assert_equals(0, len(words))
    
    # Build a pmap manually
    pmap = { '':['a'], 'a':['','t'], 'at':[''] }
    words =  a4.pmap_to_word_list(pmap)
    assert_lists_equal(['a', 'at'], words)
    
    # See if we can go back and forth
    expected = ['the', 'be','to','of','and','a','in','that','have','it']
    pmap  = a4.word_list_to_pmap(expected)
    words = a4.pmap_to_word_list(pmap)
    assert_lists_equal(expected, words)
    
    print 'pmap_to_word_list is working correctly'

def test_pmap_has_word():
    """Test function pmap_has_word"""
    print 'Testing function pmap_has_word'
    
    # Start with an empty prefix map
    pmap = {}
    cornelltest.assert_false(a4.pmap_has_word(pmap, 'a'))
    
    # Build a pmap manually
    pmap = { '':['a'], 'a':['','t'], 'at':[''] }
    cornelltest.assert_false(a4.pmap_has_word(pmap, '')) # NOT A WORD
    cornelltest.assert_false(a4.pmap_has_word(pmap, 'by'))
    cornelltest.assert_true(a4.pmap_has_word(pmap, 'a'))
    cornelltest.assert_true(a4.pmap_has_word(pmap, 'at'))
    
    print 'pmap_has_word is working correctly'


def test_autocomplete():
    """Test search function autocomplete"""
    
    print 'Testing function autocomplete'
    
    pmap = {} 
    assert_lists_equal([], (a4.autocomplete('e',pmap))) #case with empty pmap
    
    pmap = a4.word_list_to_pmap(a4.build_word_list('short.txt')) 
    assert_lists_equal(['the','that'], (a4.autocomplete('th', pmap))) #two words from prefix
    assert_lists_equal(['be'], (a4.autocomplete('b',pmap))) #one word from prefix
    assert_lists_equal([], (a4.autocomplete('xxx',pmap))) #no words from prefix
    assert_lists_equal(['a','and'], (a4.autocomplete('a',pmap))) #one letter word, greater than one letter word
    assert_lists_equal(['the', 'to','that'], (a4.autocomplete('t',pmap))) #three words created
    print 'autocomplete is working correctly'


def test_scrabble():
    """Test search function scrabble"""
    
    print 'Testing function scrabble'
    
    pmap = a4.word_list_to_pmap(a4.build_word_list('short.txt'))
    assert_lists_equal(['be','to'], (a4.scrabble('theob',2,pmap))) #two words made
    assert_lists_equal(['that'], (a4.scrabble('thiat',4,pmap))) #one word made
    assert_lists_equal(['have','that'], (a4.scrabble('hattve',4,pmap))) #same letters, two words made
    assert_lists_equal([], (a4.scrabble('rjlksdfklj',0,pmap))) # size of length 0
    assert_lists_equal([], (a4.scrabble('',4,pmap))) #empty rack
    assert_lists_equal([], (a4.scrabble('xxx',2,pmap))) #no words can be made
    assert_lists_equal([], (a4.scrabble('the',0,pmap))) #word in pmap but size is 0
    
    pmap = {}
    assert_lists_equal([], (a4.scrabble('catz',3,pmap))) #empty pmap
    
    print 'scrabble is working correctly' 
    

def test_match():
    """Test search function match"""
    
    print 'Testing function match'
    
    pmap = a4.word_list_to_pmap(a4.build_word_list('short.txt'))
    assert_lists_equal(['in','it'], (a4.match('i?',pmap))) # two words match template
    assert_lists_equal(['to'], (a4.match('t?',pmap))) # '? as last character
    assert_lists_equal([], (a4.match('',pmap))) #empty template
    assert_lists_equal(['and'], (a4.match('?nd',pmap))) # '?' as first character
    assert_lists_equal(['a'], (a4.match('?',pmap))) #one letter word
    
    pmap = {}
    assert_lists_equal([], (a4.match('?',pmap))) #empty pmap
    
    print 'match is working correctly'


# Application Code
if __name__ == "__main__":
    # Part A
    test_build_word_list()
    test_word_list_by_size()
    test_word_list_extend()

    # Part B
    test_pmap_add_word()
    test_word_list_to_pmap()
    test_pmap_to_word_list()
    test_pmap_has_word()
    
    # Part C
    test_autocomplete()
    
    # Part D
    test_scrabble()
    test_match()
    print "Module a4 is working correctly"
