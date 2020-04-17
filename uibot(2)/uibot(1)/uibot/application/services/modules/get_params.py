from application.utils.parse_data import handle_request_data,handle_response_data
from application.utils.configlogger import loger
from application.utils.errors import CustomFlaskError
from application.data import db_session,ModulesOrders
from application.Enums.eums import RespEnum
logging = loger

# 获取测试参数
def get_order_params():

    '''
    :param:
    :return:
    '''
    test_params_dict = handle_request_data()
    module_name = test_params_dict.get("module_name",None)
    order_name = test_params_dict.get("order_name",None)
    if order_name and module_name:
        with db_session() as sess:
            query_result = sess.query(ModulesOrders.pre_parameter,ModulesOrders.test_parameter,ModulesOrders.bh_parameter)\
                                                                        .filter(ModulesOrders.order_name_chn == order_name,ModulesOrders.module_name_chn == module_name)\
                                                                        .first()
            logging.info(f"{order_name}的参数查询结果:{query_result}")


        parameter_name = ["prepose_parameter","test_parameter","bh_parameter"]
        if query_result:
            value_list = [ item for item in query_result]
            result_list = zip(parameter_name,value_list)
            return handle_response_data(result_list)
        else:
            raise CustomFlaskError(RespEnum.ERR_00000012[0],RespEnum.ERR_00000012[1])
