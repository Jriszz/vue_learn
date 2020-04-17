from flask import request,jsonify
def user_login():
    user_dict = get_params()
    res_token = user_dict.get('token',None)
    res =  jsonify(user_dict)
    res.status_code = 200
    return res
def get_params():
    '''

    :return: request_args_dict type dict
    '''
    request_args_dict = dict()
    if request.args:
        request_args_dict.update(request.args.to_dict())
    elif request.form:
        request_args_dict.update(request.form.to_dict())
    elif request.is_json:
        request_args_dict.update(request.get_json())
    return request_args_dict
