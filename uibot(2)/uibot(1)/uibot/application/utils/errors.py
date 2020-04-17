from flask import jsonify

class CustomFlaskError(Exception):
    '''
        :param resp_code 错误返回码
        :param resp_desc 错误描述
        :param payload 详细错误

    '''
    __slots__ = ('resp_code','resp_desc','payload')
    def __init__(self,resp_code, resp_desc, payload=None):
        self.resp_code = resp_code
        self.resp_desc = resp_desc
        self.payload = payload
    def to_dict(self):
        temp_dict = dict()
        temp_dict['resp_code'] = self.resp_code
        temp_dict['resp_desc'] = self.resp_desc
        if self.payload is not None:
            temp_dict['payload'] = self.payload
        return temp_dict
