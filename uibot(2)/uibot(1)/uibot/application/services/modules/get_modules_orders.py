from application.utils.configlogger import loger
from application.utils.errors import CustomFlaskError
from application.data import db_session,ModulesOrders
from application.utils.parse_data import handle_request_data,handle_response_data
from application.Enums.eums import RespEnum


logging = loger
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
        #查询数据
        with db_session() as sess:
            query_result = sess.query(ModulesOrders.module_name_chn).all()
            logging.info(f"所有模块名查询结果：{query_result}")
        #获取所有模块
        all_module = set(query_result)
        #创建返回参数
        modules_name_list = [ item[0] for item in all_module ]
        response_parmeter = [("modules_name",modules_name_list)]
        return handle_response_data(response_parmeter)

def get_orders():
    '''
    :param: modules_name
    :return: all_orders
    '''
    module_name_dict = handle_request_data()
    module_name_chn = module_name_dict.get("module_name",None)


    # 获取该模块下的所有指令
    if module_name_chn:

        with db_session() as sess:

                query_result = sess.query(ModulesOrders.order_name_chn).filter(ModulesOrders.module_name_chn==module_name_chn).all()
                logging.info(f"{module_name_chn}下的命令包括{query_result}")

        orders_name_list = [item[0] for item in query_result]
        response_parameter = [("orders_name",orders_name_list)]

        return handle_response_data(response_parameter)
    else:
        raise CustomFlaskError(RespEnum.ERR_00000011[0],RespEnum.ERR_00000011[1],"module_name")
