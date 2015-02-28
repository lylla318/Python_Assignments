# a3test.py
# Lylla Younes ley23 
# 10/10/14
""" Unit Test for Assignment A3"""
import colormodel
import cornelltest
import a3

def test_complement():
    """Test function complement"""
    
    print 'Testing function complement'
    
    cornelltest.assert_equals(colormodel.RGB(255-250, 255-0, 255-71), 
            a3.complement_rgb(colormodel.RGB(250, 0, 71)))
    cornelltest.assert_equals(colormodel.RGB(255-0, 255-0, 255-0), 
            a3.complement_rgb(colormodel.RGB(0, 0, 0)))
    cornelltest.assert_equals(colormodel.RGB(255-255, 255-255, 255-255), 
            a3.complement_rgb(colormodel.RGB(255, 255, 255)))
    
    


def test_truncate5():
    """Test function truncate5"""
    
    print 'Testing function truncate5'
    
    cornelltest.assert_equals('130.5',  a3.truncate5(130.59))
    cornelltest.assert_equals('130.5',  a3.truncate5(130.54))
    cornelltest.assert_equals('100.0',  a3.truncate5(100))
    cornelltest.assert_equals('99.56',  a3.truncate5(99.566))
    cornelltest.assert_equals('99.99',  a3.truncate5(99.99))
    cornelltest.assert_equals('99.99',  a3.truncate5(99.995))
    cornelltest.assert_equals('21.99',  a3.truncate5(21.99575))
    cornelltest.assert_equals('21.99',  a3.truncate5(21.994))
    cornelltest.assert_equals('10.01',  a3.truncate5(10.013567))
    cornelltest.assert_equals('10.00',  a3.truncate5(10.000000005))
    cornelltest.assert_equals('9.999',  a3.truncate5(9.9999))
    cornelltest.assert_equals('9.999',  a3.truncate5(9.9993))
    cornelltest.assert_equals('1.354',  a3.truncate5(1.3546))
    cornelltest.assert_equals('1.354',  a3.truncate5(1.3544))
    cornelltest.assert_equals('0.045',  a3.truncate5(.0456))
    cornelltest.assert_equals('0.045',  a3.truncate5(.0453))
    cornelltest.assert_equals('0.005',  a3.truncate5(.0056))
    cornelltest.assert_equals('0.001',  a3.truncate5(.0013))
    cornelltest.assert_equals('0.000',  a3.truncate5(.0004))
    cornelltest.assert_equals('0.000',  a3.truncate5(.0009999))


def test_round5():
    """Test function round5"""
    
    print 'Testing function round5'
    
    cornelltest.assert_equals('130.6',  a3.round5(130.59))
    cornelltest.assert_equals('130.5',  a3.round5(130.54))
    cornelltest.assert_equals('100.0',  a3.round5(100))
    cornelltest.assert_equals('99.57',  a3.round5(99.566))
    cornelltest.assert_equals('99.99',  a3.round5(99.99))
    cornelltest.assert_equals('100.0',  a3.round5(99.995))
    cornelltest.assert_equals('22.00',  a3.round5(21.99575))
    cornelltest.assert_equals('21.99',  a3.round5(21.994))
    cornelltest.assert_equals('10.01',  a3.round5(10.013567))
    cornelltest.assert_equals('10.00',  a3.round5(10.000000005))
    cornelltest.assert_equals('10.00',  a3.round5(9.9999))
    cornelltest.assert_equals('9.999',  a3.round5(9.9993))
    cornelltest.assert_equals('1.355',  a3.round5(1.3546))
    cornelltest.assert_equals('1.354',  a3.round5(1.3544))
    cornelltest.assert_equals('0.046',  a3.round5(.0456))
    cornelltest.assert_equals('0.045',  a3.round5(.0453))
    cornelltest.assert_equals('0.006',  a3.round5(.0056))
    cornelltest.assert_equals('0.001',  a3.round5(.0013))
    cornelltest.assert_equals('0.000',  a3.round5(.0004))
    cornelltest.assert_equals('0.001',  a3.round5(.0009999))


def test_round5_color():
    """Test the round5 functions for cmyk and hsv."""
    
    print 'Testing function round5_color'
    
    cornelltest.assert_equals('(98.45, 25.36, 72.80, 25.00)',
            a3.round5_cmyk(colormodel.CMYK(98.448, 25.362, 72.8, 25.0)));
    
    cornelltest.assert_equals('(0.000, 100.0, 100.0, 0.000)',
            a3.round5_cmyk(colormodel.CMYK(0.0004, 99.999, 99.999, 0.0002)));
    
    cornelltest.assert_equals('(332.6, 0.468, 0.226)',
            a3.round5_hsv(colormodel.HSV(332.56, 0.4679, 0.2261)));
    
    cornelltest.assert_equals('(23.00, 0.200, 0.600)',
            a3.round5_hsv(colormodel.HSV(23, 0.2, 0.5999)));
            
 


def test_rgb_to_cmyk():
    """Test rgb_to_cmyk"""
    
    print 'Testing function rgb_to_cmyk'
    
    rgb = colormodel.RGB(255, 255, 255);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.round5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.yellow))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.black))
    
    rgb = colormodel.RGB(0, 0, 0);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.round5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.yellow))
    cornelltest.assert_equals('100.0', a3.round5(cmyk.black))
        
    rgb = colormodel.RGB(217, 43, 164);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.round5(cmyk.cyan))
    cornelltest.assert_equals('80.18', a3.round5(cmyk.magenta))
    cornelltest.assert_equals('24.42', a3.round5(cmyk.yellow))
    cornelltest.assert_equals('14.90', a3.round5(cmyk.black))
    
    rgb = colormodel.RGB(51, 51, 51);
    cmyk = a3.rgb_to_cmyk(rgb)
    cornelltest.assert_equals('0.000', a3.round5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.yellow))
    cornelltest.assert_equals('80.00', a3.round5(cmyk.black))
    
    rgb = colormodel.RGB(24, 201, 24);
    cmyk = a3.rgb_to_cmyk(rgb)
    cornelltest.assert_equals('88.06', a3.round5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.magenta))
    cornelltest.assert_equals('88.06', a3.round5(cmyk.yellow))
    cornelltest.assert_equals('21.18', a3.round5(cmyk.black))


def test_cmyk_to_rgb():
    """Test translation function cmyk_to_rgb"""
    
    print 'Testing function cmyk_to_rgb'
    
    cmyk = colormodel.CMYK(18.13, 67.50, 23.12, 95.63)
    rgb = a3.cmyk_to_rgb(cmyk)
    cornelltest.assert_equals(9, rgb.red)
    cornelltest.assert_equals(4, rgb.green)
    cornelltest.assert_equals(9, rgb.blue)
    
    cmyk = colormodel.CMYK(0, 0, 100, 100)
    rgb = a3.cmyk_to_rgb(cmyk)
    cornelltest.assert_equals(0, rgb.red)
    cornelltest.assert_equals(0, rgb.green)
    cornelltest.assert_equals(0, rgb.blue)
    
    cmyk = colormodel.CMYK(100, 100, 100, 100)
    rgb = a3.cmyk_to_rgb(cmyk)
    cornelltest.assert_equals(0, rgb.red)
    cornelltest.assert_equals(0, rgb.green)
    cornelltest.assert_equals(0, rgb.blue)
    
    cmyk = colormodel.CMYK(0, 0, 0, 0)
    rgb = a3.cmyk_to_rgb(cmyk)
    cornelltest.assert_equals(255, rgb.red)
    cornelltest.assert_equals(255, rgb.green)
    cornelltest.assert_equals(255, rgb.blue)


def test_rgb_to_hsv():
    """Test translation function rgb_to_hsv"""
    
    print 'Testing function rgb_to_hsv'
    
    rgb = colormodel.RGB(183, 183, 183)
    hsv = a3.rgb_to_hsv(rgb)
    cornelltest.assert_equals('0.000', a3.round5(hsv.hue))
    cornelltest.assert_equals('0.000', a3.round5(hsv.saturation))
    cornelltest.assert_equals('0.718', a3.round5(hsv.value))
    
    rgb = colormodel.RGB(70, 30, 100)
    hsv = a3.rgb_to_hsv(rgb)
    cornelltest.assert_equals('274.3', a3.round5(hsv.hue))
    cornelltest.assert_equals('0.700', a3.round5(hsv.saturation))
    cornelltest.assert_equals('0.392', a3.round5(hsv.value))
    
    rgb = colormodel.RGB(0, 0, 0)
    hsv = a3.rgb_to_hsv(rgb)
    cornelltest.assert_equals('0.000', a3.round5(hsv.hue))
    cornelltest.assert_equals('0.000', a3.round5(hsv.saturation))
    cornelltest.assert_equals('0.000', a3.round5(hsv.value))
    
    rgb = colormodel.RGB(255, 255, 255)
    hsv = a3.rgb_to_hsv(rgb)
    cornelltest.assert_equals('0.000', a3.round5(hsv.hue))
    cornelltest.assert_equals('0.000', a3.round5(hsv.saturation))
    cornelltest.assert_equals('1.000', a3.round5(hsv.value))
    
    rgb = colormodel.RGB(100, 100, 100)
    hsv = a3.rgb_to_hsv(rgb)
    cornelltest.assert_equals('0.000', a3.round5(hsv.hue))
    cornelltest.assert_equals('0.000', a3.round5(hsv.saturation))
    cornelltest.assert_equals('0.392', a3.round5(hsv.value))
    
    


def test_hsv_to_rgb():
    """Test translation function hsv_to_rgb"""
    
    print 'Testing function hsv_to_rgb'
    
    hsv = colormodel.HSV(357.7, 0.500, 1.000)
    rgb = a3.hsv_to_rgb(hsv)
    cornelltest.assert_equals(255, rgb.red)
    cornelltest.assert_equals(128, rgb.green)
    cornelltest.assert_equals(132, rgb.blue)
    
    hsv = colormodel.HSV(140.6, 0.265, 0.975)
    rgb = a3.hsv_to_rgb(hsv)
    cornelltest.assert_equals(183, rgb.red)
    cornelltest.assert_equals(249, rgb.green)
    cornelltest.assert_equals(205, rgb.blue)
    
    hsv = colormodel.HSV(0.000, 0.000, 0.000)
    rgb = a3.hsv_to_rgb(hsv)
    cornelltest.assert_equals(0, rgb.red)
    cornelltest.assert_equals(0, rgb.green)
    cornelltest.assert_equals(0, rgb.blue)
    
    hsv = colormodel.HSV(180.0, 1.000, 1.000)
    rgb = a3.hsv_to_rgb(hsv)
    cornelltest.assert_equals(0, rgb.red)
    cornelltest.assert_equals(255, rgb.green)
    cornelltest.assert_equals(255, rgb.blue)
    
    hsv = colormodel.HSV(180.0, 0.500, 0.500)
    rgb = a3.hsv_to_rgb(hsv)
    cornelltest.assert_equals(64, rgb.red)
    cornelltest.assert_equals(128, rgb.green)
    cornelltest.assert_equals(128, rgb.blue)


# Application Code
if __name__ == "__main__":
    test_complement()
    test_truncate5()
    test_round5()
    test_round5_color()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    test_rgb_to_hsv()
    test_hsv_to_rgb()
    print "Module a3 is working correctly"
