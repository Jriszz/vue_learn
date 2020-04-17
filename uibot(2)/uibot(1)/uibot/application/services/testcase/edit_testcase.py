from application.utils.parse_data import handle_request_data,handle_response_data
from application.utils.configlogger import loger
from application.data import db_session,ModulesOrders,BaseOrders



logging = loger

def add_testcase():

    '''
    :author: zz
    :time: 2020/04/16
    :param : parameter
    :return: reponse
    '''

    result = handle_request_data()

    #获取前置数据和后置数据

    prepose_parameter_dict = result["prepose_parameter"] if result.get("prepose_parameter","") else None
    post_parameter_dict =  result["post_parameter"] if result.get("post_parameter","") else None

    #获取预取数据
    if result.get("test_parameter",""):

        for index,parameter in enumerate(result["test_parameter"]):
            for key,value in parameter.items():
                if key == "expectval":
                    expect_val = value
                    result["test_parameter"].pop(index)
    else:
        expect_val = ""
    #过滤前置数据

    #过滤测试数据
    test_parameter_dict = dict()

    try:
        for parameter in result["test_parameter"]:

            for key,value in parameter.items():

                    test_parameter_dict[key] = eval(value)

    except Exception as e:
            test_parameter_dict[key] = value
            logging.error(f"数据解析错误: {e}")
    logging.info(test_parameter_dict)

    # 过滤后置数据

    #组装插入数据
    commit_data = dict()

    # 查询数据表
    with db_session() as sess:
        module_order_name = sess.query(ModulesOrders.module_name,ModulesOrders.order_name).filter(ModulesOrders.module_name_chn==result["module_name"]
                                                                                                  and ModulesOrders.order_name_chn == result["order_name"]).first()
    module_order_name_list = [ item for item in module_order_name]
    commit_data["test_module"] = result["module_name"]
    commit_data["order_name"] = module_order_name_list[1]
    commit_data["case_name"] = result["test_case"]
    commit_data["precondition"] = prepose_parameter_dict
    commit_data["test_parmeter"] = test_parameter_dict
    commit_data["comments"] = result["comment"]
    commit_data["bhcondition"] = post_parameter_dict
    commit_data["expect_val"] = expect_val
    commit_table_obj = eval(module_order_name_list[0])(**commit_data)
    logging.info(commit_data)
    logging.info("数据表对象：{}".format(str(commit_data)))

    with db_session() as sess:
        sess.add(commit_table_obj)
        sess.commit()

    return handle_response_data()

# if __name__ == "__main__":
#     USER = "test"
#     PASSWORD = "test"
#     DB_URL = "192.168.0.61:3306"
#     DATABASE_NAME = "testcasedata"
#     SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USER}:{PASSWORD}@{DB_URL}/{DATABASE_NAME}?charset=utf8"
#     commit_data = {'test_module': '基本命令', 'order_name': 'delay', 'case_name': '4535', 'precondition': '',\
#                'test_parmeter': {'delay_time': 3453}, 'comments': '45353', 'bhcondition': '', 'expect_val': '3453'}
#
#     engine = create_engine( SQLALCHEMY_DATABASE_URI, echo=True,pool_recycle=3600)
#     # ins = BaseOrders.insert()
#     # ins_val = ins.values(**commit_data)
#     seesion_db = sessionmaker(bind=engine)
#     sess = seesion_db(autocommit=True)
#     sess.add(BaseOrders(**commit_data))
#     sess.commit()
#     # print(ins_val)
#     # res = sess.execute(ins_val)
#     print(res)