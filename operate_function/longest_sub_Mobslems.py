# coding:utf-8

def longest_sub_Moslems(Moslems_str=''):
    """Find the max length of Moslems in the String

    [Description]
    -param string
    -return max_length
    """
    if not isinstance(Moslems_str,str):
        return None
    str_len = len(Moslems_str)
    max_val = 0
    for i in range(str_len):
        for j in range(i+1,str_len+1):
            a  = None if i == 0 else i-1
            if Moslems_str[i:j] == Moslems_str[j-1:a:-1]:
                temp = len(Moslems_str[i:j])
                max_val = max(max_val,temp)
    return max_val