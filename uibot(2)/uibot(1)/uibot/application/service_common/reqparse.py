from flask import request,current_app,jsonify
from werkzeug.datastructures import MultiDict,FileStorage
from werkzeug import exceptions
from copy import deepcopy


class Namespace(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except:
            raise AttributeError(name)

    def __setattr__(self, key, value):
        self[key] = value
    def __str__(self):
        return '{0}'.format(self.__class__.__name__)
_friendly_location = {
    'json': 'the JSON body'
}

class Argument(object):
    '''
    :param name: Either a name
    '''
    def parse_args(self,params_args):
        if isinstance(params_args,dict):
            return 'params_args is {0}'.format('dict')
        else:
            return 'params_args is invalid!'

def set_args():
    return jsonify({'resp_code':9000,'resp_desc':'set_args has successd'})