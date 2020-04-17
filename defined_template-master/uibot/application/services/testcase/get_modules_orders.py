from flask import make_response,jsonify
from application.data import db_session
from application.data import ModulesOrders
from application.utils.parse_data import handle_request_data,handle_response_data
import json


'''
@author: zz
@time: 
'''

def get_modules():
        '''
        :param: None
        :return: all_modules
        step: 1.查询modules_orders表
        '''
        response = make_response()
        #查询数据
        with db_session() as sess:
            modules = sess.query(ModulesOrders.module_name).all()

        #获取所有模块
        all_module = set(modules)
        #创建返回参数
        response_parmeter = dict()
        modules_name_list = [val for val in all_module]
        response_parmeter["modules_name"] = modules_name_list

        # return jsonify(response_parmeter)
        #handle_response_data(jsonify(response_parmeter))

# def get_orders():
#     '''
#
#     :return: all_orders
#     '''
#     parse_request_data
#     with