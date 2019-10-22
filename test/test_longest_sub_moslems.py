# test the longest_sub_moslems functions
from operate_function.longest_val import longest_sub_Moslems


def test_string_is_None():

    """Test the string is None

    [Description]
    --
    """
    assert 0 == longest_sub_Moslems()

def test_string_is_six():

    """Test the longest moslems is six

    [Description]
    --
    """
    assert 6 == longest_sub_Moslems('abccbabds')

def test_string_is_invalid():

    """Test the longest moslems is six

    [Description]
    --
    """
    assert None == longest_sub_Moslems([1,3,4])