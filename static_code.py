# 类名和顶行留两个空行
# 类名和函数名留一个空行
# 函数注释中summary 和函数说明
# D400 First line should end with a period //在第一行结尾缺少一个句号
from os import path


class FileParse(object):
    """This is read the files content //设置函数作用简要summary[period]2019/10/21.

    [Description] //设置函数说明
    -read the files like that xml,html
    -return the result of performance
    """

    def get_content():
        """Read the files content //设置函数作用简要summary[period]2019/10/21.

        [Description] //设置函数说明
        -read the files like that xml,html
        -return the result of performance
        """
        pass


# class FileParse2(object):

    # def get_content():
        # r"""This is read the files content //设置函数作用简要summary 2019/10/21

        # [Description] //设置函数说明
        # -read the files like that xml,html
        # -return the result of performance
        # """
        # pass
