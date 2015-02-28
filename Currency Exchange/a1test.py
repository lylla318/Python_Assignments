#module a1.py
#Lylla Younes, ley23
#9/16/2014
"""Unit test for module a1

When run as a script, this module invokes several procedures that 
test the various functions in the module a1."""

import cornelltest
import a1

def testA():
    
    print 'Testing function after_space()'
    s = 'The happy cheeseburger'
    result=a1.after_space(s)
    cornelltest.assert_equals('happy cheeseburger',result)
    
    s = 'The   happy cheeseburger'
    result=a1.after_space(s)
    cornelltest.assert_equals('  happy cheeseburger',result)
    
    s = 'The  '
    result=a1.after_space(s)
    cornelltest.assert_equals(' ',result)
    
    print 'Testing function before_comma_or_end()'
    s = 'The, hungry programmer'
    result=a1.before_comma_or_end(s)
    cornelltest.assert_equals('The',result)
    
    s = 'The juicy cheeseburger'
    result=a1.before_comma_or_end(s)
    cornelltest.assert_equals('The juicy cheeseburge',result)
    
    s = 'The happy, hungry,cheeseburger'
    result=a1.before_comma_or_end(s)
    cornelltest.assert_equals('The happy',result)
    
    s = 'The happy,, hungry'
    result=a1.before_comma_or_end(s)
    cornelltest.assert_equals('The happy',result)



def testB():
    
    print 'Testing function get_keyword_index'
    json ='Cars "beat" Trucks'
    result = a1.get_keyword_index(json,'beat')
    cornelltest.assert_equals(5,result)
    
    json ='A then "E" then I'
    result = a1.get_keyword_index(json,'E')
    cornelltest.assert_equals(7,result)
    
    json ='A x B "key" C'
    result = a1.get_keyword_index(json,'x')
    cornelltest.assert_equals(-1,result)
    
    print 'Testing function has_error()'
    json ='{"to": <code>, "rate": <value>, "warning": <message>,"from": <code>}'
    result = True
    cornelltest.assert_equals(True,result)
    
    json ='{"err":<description>}'
    result = True
    cornelltest.assert_equals(True,result)
    
    json ='{"to": "ARS", "rate": 8.415000, "from": "USD", \
          "v": 1.93007500000000}'
    result = False
    cornelltest.assert_equals(False,result)
    
    print 'Testing funtion get_value()'
    json = '{"to": "EUR", "rate": 0.444586, "from": "USD", \
           "v": 1.93875900000000}'
    result = a1.get_value(json,'to')
    cornelltest.assert_equals('"EUR"',result)
    
    json = '{"to": "EUR", "rate": 0.444586, "from": "USD", \
           "v": 1.93875900000000}'
    result = a1.get_value(json,'rate')
    cornelltest.assert_equals('0.444586',result)
    

def testC():
    print 'Testing function currency_response'
    result = a1.currency_response('XYZ', 'CLP', 14.6)
    cornelltest.assert_equals('{"err": "failed to parse response from xe.com."}', result)

def testD():
    print 'Testing function iscurrency'
    result = a1.iscurrency('EUR')
    cornelltest.assert_equals(True, result)
    
    result = a1.iscurrency('XYZ')
    cornelltest.assert_equals(False, result)
    
    result = a1.iscurrency('...')
    cornelltest.assert_equals(False, result)
    
    print 'Testing function exchange'
    result = a1.exchange('USD', 'USD', 1.00)
    cornelltest.assert_floats_equal(1.00, result)
    
    print 'Testing function exchange'
    result = a1.exchange('EUR', 'USD', 18.97)
    cornelltest.assert_floats_equal(24.57158400580288, result)
    
    print 'Testing function exchange'
    result = a1.exchange('USD', 'USD', 1.00)
    cornelltest.assert_floats_equal(1.00, result)
    
    

if __name__ == '__main__':
    testA()
    testB()
    testC()
    testD()
    print "Module a1 passed all tests"
