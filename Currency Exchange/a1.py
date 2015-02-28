#module a1.py
#Lylla Younes, ley23
#9/16/2014
"""Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange."""

#Part A

def after_space(s):
    """Returns: The substring of s after the first space.
    
    Precondition: s is a string with at least one space in it."""
    
    first_index = s.find(" ")
    inner= s[first_index+1:]
    
    return inner
    
    
def before_comma_or_end(s):
    """Returns: Substring of s up to but not including, the first comma.
    
    Precondition: s is a nonempty string"""
    
    first_index=s.find(",")
    inner=s[:first_index]
    
    return inner

#Part B


def get_keyword_index(json,key):
    """Returns: The index of the given key inside the JSON string 
    (including the quote character). It returns -1 if key is not there.
    
    Precondition: key is a string that does not contain double quotes, 
    while json is a string."""
    
    return json.find('"'+key+'"')
    
    
def has_error(json):
    """Returns: True if json is an invalid response, and False otherwise.
    
    Precondition: json is the response to a currency query."""
    
    return json.find('warning')!= -1 or json.find('err')!= -1

    
def get_value(json,key):
    
    """Returns: The JSON value (as a string) associated with the given key.
    
    Precondition: key is a string that does not contain double quotes,
    while json is a JSON response string that has key as a valid keyword."""
    
    quote_key = '"'+key+'"'    
    first_index = json.find(quote_key)
    second_index = json.find(':', first_index+len(quote_key))
    third_index = json.find(',', second_index+1)
    return json[second_index+1:third_index].strip()

#Part C

import urllib2

def currency_response(currency_from, currency_to, amount_from):
    """Returns: a JSON string that is a response to a currency query.
    
    Precondition: currency_from and currency_to are of type string,
    while amount_from is a float."""
    
    json = 'http://cs1110.cs.cornell.edu/2014fa/a1/calculator.php?'
    url = json + 'from=' + currency_from + '&to=' + currency_to +\
          '&q='+ str(amount_from)
    info = urllib2.urlopen(url)
    return info.read()

#Part D

def iscurrency(currency):
    """Returns: True if currency is a valid (3 letter code for a) currency. 
    It returns False otherwise.

    Precondition: currency is a string."""
    
    json = currency_response(currency, currency,1.00)
    result = has_error(json)
    return not result
    
    
    
def exchange(currency_from, currency_to, amount_from):
    a=1
    
    
    """Returns: amount of currency received in the given exchange.
    Precondition: currency_from and currency_to are of type string,
    and are both valid three-letter currency codes.  The value
    amount_from is a float"""
    
    json = currency_response(currency_from, currency_to, amount_from)
    return float(get_value(json,'v'))