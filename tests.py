"""
A test script to test the module funcs.py

<YOUR NAME HERE>
<DATE HERE>
"""
import introcs      # For assert_equals and assert_true
import funcs        # This is what we are testing


# TEST PROCEDURE
def test_asserts():
    """
    This is a simple test procedure to help you understand how assert works
    """
    print('Testing the introcs asserts')
    introcs.assert_equals('b c', 'ab cd'[1:4])
    #introcs.assert_equals('b c', 'ab cd'[1:3])

    introcs.assert_true(3 < 4)
    introcs.assert_equals(3, 1+2)

    introcs.assert_equals(3.0, 1.0+2.0)
    introcs.assert_floats_equal(6.3, 3.1+3.2)
    #introcs.assert_equals(6.4, 3.3+3.1)

def test_has_a_vowel():
    """
    This procedure tests the has_a_vowel module"""
    print('Testing function has_a_vowel')
    input='aeiou'
    result=funcs.has_a_vowel(input)
    introcs.assert_equals(True, result)

def test_replace_first():
    """ This procedure testes the replace_first module"""
    print('Testing test_replace_first')
    result=funcs.replace_first('crane', 'a', 'o')
    introcs.assert_equals('crone', result)

# SCRIPT CODE (Call Test Procedures here)
test_asserts()
test_has_a_vowel()
test_replace_first()
print('Module funcs is working correctly')
