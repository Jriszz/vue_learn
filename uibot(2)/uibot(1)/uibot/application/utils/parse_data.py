from flask import request,make_response,jsonify,abort
from application.utils.configlogger import loger
from application.Enums import RespEnum

logging = loger

def handle_request_data():

    if request.args:
        logging.info("request parameter:{}".format(str(request.args)))
        return request.args.to_dict()
    elif request.form:
        logging.info("request parameter:{}".format(str(request.form)))
        return request.form.to_dict()
    elif request.files:
        logging.info("request parameter:{}".format(str(request.files)))
        return request.files.to_dict()
    elif request.json:
        logging.info("request parameter:{}".format(str(request.json)))
        return request.json
    elif request.data:
        logging.info("request parameter:{}".format(str(request.data)))
        return request.data

    abort(500)

def handle_response_data(response_parmeter:list=[]):

    response_data = dict()
    if response_parmeter:
        response_data = { key :value for key,value in [item for item in response_parmeter]}
    response_data["resp_desc"] = RespEnum.Succ_00000000[1]
    response_data["resp_code"] = RespEnum.Succ_00000000[0]
    response = make_response(jsonify(response_data))
    response.headers["Accept-Ranges"] = "application/json"
    response.headers["Content-type"] = "application/json"
    logging.info(f"返回结果:{response}")
    return response

