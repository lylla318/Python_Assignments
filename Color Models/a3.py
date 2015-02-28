# a3.py
# LYLLA YOUNES ley23    
# 10/10/14
""" Functions for Assignment A3"""
import colormodel
import math

def complement_rgb(rgb):
    """Returns: the complement of color rgb.
    
    Precondition: rgb is an RGB object"""
    # We asserted this precondition for you.  You do not need to do anything here.
    assert (type(rgb) == colormodel.RGB), 'Value '+ `rgb`+' is not a RGB object'
    
    # THIS IS WRONG.  FIX IT
    return colormodel.RGB(255-rgb.red, 255-rgb.green, 255-rgb.blue)


def truncate5(value):
    """Returns: value, as a string, using exactly 5 characters.
    
    The truncated value will have one of the forms:
       ddd.d      Example:  360.1
       dd.dd      Example:  29.53
       d.ddd      Examples: 4.003,  0.001,  and 0.000
    
    Precondition: value is a number (int or float), 0 <= value <= 999."""
    # To get the desired output, do the following
    #   1. Make sure value is a float.  If it is not, convert it to one.
    #   1. If value < 0.001, set value to 0.
    #      This prevents value appearing in scientific notation, e.g. 1.5E-6.
    #   2. Convert value to a string s, in the usual way. Note that s is guaranteed to
    #      have at least three chars: a decimal point and a digit on either side of it.
    #      Therefore, the simplest thing to do as s is being constructed is to make
    #      sure s has at least 5 chars by appending "00" after the decimal point.
    #   3. Return the first five characters of s.
    
    assert (type(value) == int or type(value) == float), str(value) + ' is not of type int or float'
    assert (value >= 0 and value <= 999), str(value) + ' is not in range 0 to 999'
    
    value1 = float(value)
    if value1 < 0.001:
        value1 = 0.00
    s = str(value1) + '00'
    value1 = s[:5]
    #print value1
 
    return value1


def round5(value):
    """ Returns: value, as a string, but expand or round to be (if necessary) 
    exactly 5 characters.
    
    Examples:
       Round 1.3546  to  1.355.
       Round 1.3544  to  1.354.
       Round 21.9954 to  22.00.
       Round 21.994  to  21.99.
       Round 130.59  to  130.6.
       Round 130.54  to  130.5.
       Round 1       to  1.000.
    
    Precondition: value is a number (int or float), 0 <= value <= 360."""
    
    assert (type(value) == int or type(value) == float), str(value) + ' is not an int or float'
    assert (value >= 0 and value <= 360), str(value) + ' is not in range 0 to 360'
  
    # MAKE SURE THAT VALUE IS A FLOAT BEFORE USING THE BUILT-IN round() FUNCTION
    # If it is not a float convert it to one with the float() function.
    #value1 = truncate5(value)
    
    value1 = float(value)
    
    if value1 >= 0 and value1 < 10:
        value2 = round(value1,3)
        return truncate5(value2)
    
    elif value1 >= 10 and value1 < 100:
        value2 = round(value1,2)
        return truncate5(value2)
    
    elif value1 >= 100:
        value2 = round(value1,1)
        return truncate5(value2)


def round5_cmyk(cmyk):
    """Returns: String representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Precondition: cmyk is an CMYK object."""
    
    assert (type(cmyk) == colormodel.CMYK), str(cmyk) + 'is not a CMYK object'
    
    C = round5(cmyk.cyan)
    M = round5(cmyk.magenta)
    Y = round5(cmyk.yellow)
    K = round5(cmyk.black)
    
    return '(' + C + ', ' + M + ', ' + Y + ', ' + K + ')'


def round5_hsv(hsv):
    """Returns: String representation of hsv in the form "(H, S, V)".
    
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    
    Precondition: hsv is an HSV object."""
    assert (type(hsv) == colormodel.HSV), str(hsv) + 'is not a HSV object'
    
    H = round5(hsv.hue)
    S = round5(hsv.saturation)
    V = round5(hsv.value)
    
    return '(' + H + ', ' + S + ', ' + V + ')'


def rgb_to_cmyk(rgb):
    """Returns: color rgb in space CMYK, with the most black possible.
    
    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
    
    Precondition: rgb is an RGB object"""
    assert (type(rgb) == colormodel.RGB), str(rgb) + 'is not a RGB object'
    
    C1 = 1 - rgb.red/255.0
    M1 = 1 - rgb.green/255.0
    Y1 = 1 - rgb.blue/255.0
    
    if C1 == 1 and M1 == 1 and Y1 == 1:
        return colormodel.CMYK(0.0, 0.0, 0.0, 100.0)
    else:
        list_K = [C1, M1, Y1]
        K = min(list_K)
        C = ((C1 - K)/(1 - K)) * 100
        M = ((M1 - K)/(1 - K)) * 100
        Y = ((Y1 - K)/(1 - K)) * 100
        K = K * 100
        
        return colormodel.CMYK(C, M, Y, K)
        
        


def cmyk_to_rgb(cmyk):
    """Returns : color CMYK in space RGB.
    
    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
    
    Precondition: cmyk is an CMYK object."""
    
    assert (type(cmyk) == colormodel.CMYK), str(cmyk) + 'is not a CMYK object'
    
    C = cmyk.cyan/100.0
    M = cmyk.magenta/100.0
    Y = cmyk.yellow/100.0
    K = cmyk.black/100.0
    
    R = ((1 - C)*(1 - K))*255.0
    G = ((1 - M)*(1 - K))*255.0
    B = ((1 - Y)*(1 - K))*255.0
    
    final_R = int(round(R,0))
    final_G = int(round(G,0))
    final_B = int(round(B,0))
    
    return colormodel.RGB(final_R, final_G, final_B)


def rgb_to_hsv(rgb):
    """Return: color rgb in HSV color space.
    
    Formulae from wikipedia.org/wiki/HSV_color_space.
    
    Precondition: rgb is an RGB object"""
    
    assert (type(rgb) == colormodel.RGB), str(rgb) + 'is not a RGB object'
    
    r1 = rgb.red/255.0
    g1 = rgb.green/255.0
    b1 = rgb.blue/255.0
    list_rgb = [r1,g1,b1]
    max_list = max(list_rgb)
    min_list = min(list_rgb)
    
    if max_list == min_list:
        h1 = 0
    elif max_list == r1 and g1 >= b1:
        h1 = (60.0 * (g1 - b1))/(max_list - min_list)
    elif max_list == r1 and g1 < b1:
        h1 = ((60.0 * (g1 - b1))/(max_list - min_list)) + 360.0
    elif max_list == g1:
        h1 = ((60.0 * (b1 - r1))/(max_list - min_list)) + 120.0
    elif max_list == b1:
        h1 = ((60.0 * (r1 - g1))/(max_list - min_list)) + 240.0
        
    if max_list == 0:
        s1 = 0
    else:
        s1 = 1 - (min_list/max_list)
        
    v1 = max_list
    
    
    return colormodel.HSV(h1, s1, v1)


def hsv_to_rgb(hsv):
    """Returns: color in RGB color space.
    
    Formulae from http://en.wikipedia.org/wiki/HSV_color_space.
    
    Precondition: hsv is an HSV object."""
    
    assert (type(hsv) == colormodel.HSV), str(hsv) + 'is not a HSV object'
    
    h = hsv.hue
    s = hsv.saturation
    v = hsv.value
    
    h_i = math.floor(hsv.hue/60)
    f = (hsv.hue/60) - h_i
    p = hsv.value * (1 - hsv.saturation)
    q = hsv.value * (1 - (f * hsv.saturation))
    t = hsv.value * (1 - ((1 - f) * hsv.saturation))
    
    if h_i == 0:
        R = v
        G = t
        B = p
    elif h_i == 1:
        R = q
        G = v
        B = p
    elif h_i == 2:
        R = p
        G = v
        B = t
    elif h_i == 3:
        R = p
        G = q
        B = v
    elif h_i == 4:
        R = t
        G = p
        B = v 
    elif h_i == 5:
        R = v
        G = p
        B = q
    
    round_R = round(R*255)
    round_G = round(G*255)
    round_B = round(B*255)
    
    final_R = int(round_R)
    final_G = int(round_G)
    final_B = int(round_B)
    
    return colormodel.RGB(final_R, final_G, final_B)



