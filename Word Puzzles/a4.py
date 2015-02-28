# a4.py
# LYLLA YOUNES, ley23
# DATE COMPLETED HERE
""" Functions for Assignment A4"""


# Task 1: Word Lists

def build_word_list(filename):
    """Returns a list of words from the given file
    
    Each word in the file should be stored on a separate line. The lines are trimmed 
    to remove trailing spaces and line returns. 
    
    Example: build_word_list('short.txt') returns the 10 element list of words
    ['the','be','to','of','and','a','in','that','have','it'].
    
    Precondition: filename is the name of a text file storing a list of words.
    
    Enforced Precondition: filename is a string"""
    
    assert (type(filename) == str), str(filename) + 'is not a string'
    

    items = open(filename).readlines()
    w_list = []

    for k in range(len(items)):
        w_list.append(items[k].strip('\n'))
    return w_list

    f_open.close()   
    


def word_list_by_size(words, size):
    """Returns the elements of words that have length size
    
    The words in the resulting list should be in the same order as the original list.
    
    Example: word_list_by_size(['a', 'at', 'axe', 'by'], 2) returns ['at','by']
    
    Precondition: words is a list of strings. size is a positive int.
    
    Enforced Precondition: words is a list. size is a positive int."""
    
    assert (type(words) == list), str(words) + 'is not a list'
    assert (type(size) == int), str(size) + 'is not an int'
    assert (int(size) > 0), str(size) + 'is not positive'
    
    new_list = []
    for k in range(len(words)):
        if len(words[k]) == size:
            new_list.append(words[k])
            
    return new_list   
    
    


def word_list_extend(words, prefix):
    """Returns the word list that is the result of adding prefix to the start of 
    every word in the list words.
    
    The resulting word list is sorted alphabetically.
    
    Example: word_list_extend(['at', 'rap'], 'c') returns ['cat', 'crap'].
    
    Precondition: words is a list of strings. prefix is a string.
    
    Enforced Precondition: words is a list. prefix is a string."""
    
    assert (type(words) == list), str(words) + 'is not a list'
    assert (type(prefix) == str), str(prefix) + 'is not a string'
    
    new_list = []
    for k in range(len(words)):
        new_list.append(prefix + words[k])
        
    return new_list
    
    
    




# Task 2: Prefix Maps

def pmap_add_word(pmap,word):
    """Adds a single word to a prefix map.
    
    This is a procedure.  It modifies the contents of pmap. It does not return.
    a new prefix map.  
    
    This function will add the word AND all of its prefixes to pmap.  For each
    prefix it will add the next letter to the list of values.  For the complete word, 
    it will add '' to the list of values. 
    
    This function does not add duplicates to the prefix map.  If a letter is already
    in the list for a given prefix map, then it will not add it a second time.
    
    Example: If pmap is the empty map {}, then pmap_add_word(pmap,'at') changes
    pmap to the dictionary { '':['a'], 'a':['t'], 'at':[''] }.

    Example: If pmap is { '':['a'], 'a':['t'], 'at':[''] }, pmap_add_word(pmap,'as') 
    changes pmap to { '':['a'], 'a':['s', 't'], 'at':[''], 'as':[''] }.
    
    Precondition: pmap is a prefix map.  word is a string with only letters.
    
    Enforced Precondition: pmap is a dict. word is a string with only letters."""
    
    assert (type(pmap) == dict), str(pmap) + 'is not a dict'
    assert (type(word) == str), str(word) + 'is not a string'
    
    
    key = ''
    value = []
    for k in range(len(word)+1):
        if k == 0:
            key = ''
            value = [word[k]]
        elif k == (len(word)):
            key = word
            value = ['']
        else:
            key = word[:k]
            value = [word[k]]
            
        if key in pmap:
            if not value[0] in pmap[key]:
                pmap[key] = pmap[key] + value
                
        else:
            pmap[key] = value
                    

def word_list_to_pmap(words):
    """Returns the prefix map for the given word list.
    
    Hint: pmap_add_word is a useful helper function.
    
    Precondition: words is a list of strings with only letters.
    '
    Enforced precondition: words is a list."""
    
    assert (type(words) == list), str(words) + 'is not a list'
    
    pmap = {}
    for k in words:
        pmap_add_word(pmap, k)
        
    return pmap
    


def pmap_to_word_list(pmap):
    """Returns the word list for the given prefix map.
    
    The word list should contain only those prefixes which have a next character
    of '' (the empty string) in the prefix map.
    
    Precondition: pmap is a prefix map.
    
    Enforced Precondition: pmap is a dict."""
    
    assert (type(pmap)==dict), str(pmap) + 'is not a dictionary'
    
    word_list = []
    for key in pmap.keys():
        if '' in pmap[key]:
            word_list.append(key)
    return word_list
            


def pmap_has_word(pmap,word):
    """Returns True if word is in the prefix map.
    
    Precondition: pmap is a prefix map.  word is a string.
    
    Enforced Precondition: pmap is a dict. word is a string."""
    
    assert (type(pmap)==dict), str(pmap) + 'is not a dictionary'
    
    word_list = pmap_to_word_list(pmap)
    
    return (word in word_list)
    

# PART C: Word Completions

def autocomplete(prefix, pmap):
    """Returns the list of all words that complete prefix in pmap
    
    If there are no words completing prefix in pmap, this function returns the
    empty list.
    
    Example: If pmap is the prefix map created from 'short.txt', then 
    autocomplete('th',pmap) returns the list ['the', 'that'].  
    Similarly, autocomplete('x',pmap) returns the empty list []
    
    Precondition: prefix is a string that is either empty or has only letters. 
    pmap is a prefix map.
    
    Enforced Preconditions: We enforce the preconditions for prefix, but only
    enforce that pmap is a dict."""
    # This function will require recursion combined with a for-loop.  The base
    # case is when prefix is not in the prefix map.  Otherwise, you will need
    # to process all of the values in the list pmap[prefix].
    
    # Be careful with pmap[prefix]. If prefix is an actual word then '' is in this
    # list.  If you are not careful with your recursive call, then you will find
    # yourself in an infinite recursion. (if only thing after prefix is empty string, just return that value (''))
    
    # NOTE: This function MUST be recurse, and you are not allowed to add any
    # helper functions to implement this function.
    
    assert (type(prefix)==str or prefix.isalpha()), str(prefix) + 'is not valid string'
    assert (type(pmap)==dict), str(pmap) + 'is not a dictionary'
    
    if not prefix in pmap:
        word_list = []
        return word_list
    
        
    word_list = []
        
    list_letters = pmap[prefix]
    list_letters2 = [] 
    
    if pmap[prefix] == ['']:
        return [prefix]

    for letter in list_letters:
        if letter == '':
            word_list = word_list + [prefix]
        else:
            word_list = autocomplete(prefix+letter, pmap) + word_list
            
    return word_list
    
    
    


# PART D: Scrabble Puzzles

def scrabble(rack,size,pmap):
    """Returns the list of all valid words that you can form from the tile rack
    using EXACTLY size letters.
        
    Example: If pmap is the prefix map created from 'short.txt', then 
    scrabble('theob',2,pmap) returns ['be', 'to'].
    
    Precondition: rack is a string that is either empty or has only letters. 
    size is a nonnegative integer. pmap is a prefix map.
   
    Enforced Precondition: We enforce the complete precondition for rack and size.
    We only enforce that pmap is a dict."""
    # We are not going to assert the preconditions here
    # We will let you do that in the helper function.
    
    
    
    return scrabble_helper('',rack,size,pmap)


def scrabble_helper(prefix,rack,size,pmap):
    """"Returns the list of all valid words extending prefix that you can form from
    the tile rack using EXACTLY size ADDITIONAL letters.
    
    The prefix map pmap is used to determine whether or not a word is valid.
    
    Example: If pmap is the prefix map created from 'short.txt', then 
    scrabble_helper('t','heob',1,pmap) returns ['to'], while 
    scrabble_helper('t','heob',2,pmap) returns ['the']

    Precondition: prefix and rack are a strings with only letters, but which may
    be empty. size is a nonnegative integer. pmap is a prefix map.
   
    Enforced Precondition: We enforce the complete precondition for prefix, rack, 
    and size. We only enforce that pmap is a dict."""
    # This function is to be implemented recursively using the process that was
    # described in the assignment overview.  At each recursive call, you will remove 
    # a letter from the rack and add it to the prefix.  Note that,  unlike scramble, 
    # size is not the number of letters in the word. It is the number of letters 
    # REMAINING to pick from the rack. So you must decrease it in the recursive call
    # as well.
    
    # This recursive function will have multiple base cases:
    
    #     1. size is 0 (so no letter left to pick)
    #     2. size > 0, but rack is empty (so there is nothing left to pick from)
    #     3. there are no words that complete prefix
    
    # In the case of 2 and 3, you should return the empty list.
    
    assert (type(pmap)==dict), str(pmap) + 'is not a dictionary'
    assert (type(prefix)==str or prefix.isalpha()), str(prefix) + 'is not valid string'
    assert (type(rack)==str or rack.isalpha()), str(rack) + 'is not valid string'
    assert (type(size)==int), str(size) + 'is not an integer'
    
    if size == 0 and (prefix in autocomplete(prefix,pmap)):
        return [prefix]
    
    if size > 0 and rack == '':
        return []
    
    if not prefix in pmap:
        return []

    
    wordlist = []

    for index in range(len(rack)):
        
        s1= rack[0:index]
        s2 = rack[index+1:]
        rack_copy = s1+s2
        
        new_word = scrabble_helper(prefix+rack[index], rack_copy, size-1, pmap)
        
        if (new_word != []):
            if (not new_word[0] in wordlist):
                wordlist = wordlist + new_word
    
    return wordlist
        
            

def match(template,pmap):
    """Returns the list of all valid words that match the given template.
    
    A template is a string combining letters and the '?' character.  A
    word is a match of for a template if it is the same length, and agrees
    with the template on every character that is not '?'. For example,
    'ate' matches the template 'a?e', as does 'axe'.
    
    The prefix map pmap is used to determine whether or not a word is valid.
    
    Example: If pmap is the prefix map created from 'short.txt', then 
    match('i?',pmap) returns ['in', 'it'].
    
    Precondition: template is a string of letters and '?'. pmap is a
    prefix map.
    
    Enforced Precondition: template is a string. pmap is a dict."""
    # We are not going to assert the preconditions here
    # We will let you do that in the helper function.
    return match_helper('',template,pmap)


def match_helper(prefix,template,pmap):
    """Returns the list of all valid words that start with the given prefix, and
    whose remaining letters match the given template.
    
    Unlike match, the template in this case is not supposed to match the whole
    string. It is only supposed to match the remaining part of the string after
    the prefix.
    
    Example: If pmap is the prefix map created from 'short.txt', then 
    match_helper('i','?',pmap) returns ['in', 'it'].
    
    Precondition: prefix is a string of letters or empty. template is either empty or
    string of letters and '?'. pmap is a prefix map.
    
    Enforced Precondition: prefix is a string of letters or empty. template is a string. 
    pmap is a dict."""
    # This function is to be implemented recursively using a process that is similar
    # to, but not the same as scrabble.  At each recursive call, you will remove
    # the first element from template.  If it is a letter, you add it to the prefix.
    # If it is a '?', you must try each valid extension of the prefix.
    
    # There are two base cases: when there are no word that complete the prefix, and 
    # when the template is empty.  In that second case, what you do depends on whether 
    # or not prefix is a word.
    
    assert (type(prefix)==str or prefix.isalpha()), str(prefix) + 'is not valid string'
    assert (type(template)==str), str(template) + 'is not a string'
    assert (type(pmap)==dict), str(pmap) + 'is not a dictionary'
    
    if autocomplete(prefix,pmap)==[]:
        return []
    
    if template == '':
        if prefix in autocomplete(prefix,pmap):
            return [prefix]
        else:
            return []
    
    wordlist = []
    
    if template[0].isalpha():
            wordlist = wordlist+ match_helper(prefix+template[0],template[1:],pmap)
    else:
        for value in pmap[prefix]:
            wordlist = wordlist+ match_helper(prefix+value,template[1:],pmap)
    
    return wordlist
            
            
                
    
    
    
    
    
    
