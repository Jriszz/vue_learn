from  application.data import db_session
from application.data.modules import ModulesOrders,BaseOrders,ExecutionConfiguration
from application.utils.parse_data import handle_request_data,handle_response_data
from application.utils.configlogger import loger

logging = loger

def find_cases():
        '''
        @author: zz
        @time: 2020/04/16
        :param: None
        :return: test_cases
        step: 1.查询modules_orders表
        '''

        #查询要执行的测试数据
        key = ("test_no", "order_name", "is_automation", "precondition", "test_parmeter","bhcondition", "is_check_data", "check_data", "expect_val", "excpect_data_val")
        with db_session() as sess:
            res = sess.query(ExecutionConfiguration.module_name,\
                             ExecutionConfiguration.order_name,\
                             ExecutionConfiguration.testcase_number)\
                            .first()

        res_list = [item for item in res]
        test_module,test_order,testcase_number = res_list;
        test_case_list = list()

        # 查询数据库中所有测试用例
        if test_module == "全部":

            # 查询所有模块,所有指令的测试用例

            with db_session() as sess:
                test_table = sess.query(ModulesOrders.module_name).all()

            test_table = set(test_table)
            logging.info(f"所有用例表测试用例:{test_table}")
            test_table_list = [item[0] for item in test_table]


            for test_table in test_table_list:



                with db_session() as sess:
                    res = sess.query(eval(test_table).test_no, \
                                     eval(test_table).order_name,\
                                     eval(test_table).is_automation,\
                                     eval(test_table).precondition, \
                                     eval(test_table).test_parmeter,\
                                     eval(test_table).bhcondition,\
                                     eval(test_table).is_check_data,\
                                     eval(test_table).check_data, \
                                     eval(test_table).expect_val,\
                                     eval(test_table).excpect_data_val).all()
            for item in res:
                parameter_dict = dict()

                parameter_dict = { key:value if value else "" for key,value in zip(key,item) }

                test_case_list.append(parameter_dict)

            logging.info(f"test_cases:{test_case_list}")

            return handle_response_data([("data_parameter",test_case_list)])



        if test_order == "全部":

            # 查询某个模块,所有指令的测试用例
            with db_session() as sess:
                test_table = sess.query(ModulesOrders.module_name)\
                    .filter(ModulesOrders.module_name_chn == test_module)\
                    .first()

            test_table_list = [item for item in test_table]
            logging.info(f"test_table_list:{test_table_list}")

            for test_table in test_table_list:

                with db_session() as sess:
                    res = sess.query(eval(test_table).test_no, \
                                     eval(test_table).order_name,\
                                     eval(test_table).is_automation,\
                                     eval(test_table).precondition, \
                                     eval(test_table).test_parmeter,\
                                     eval(test_table).bhcondition,\
                                     eval(test_table).is_check_data,\
                                     eval(test_table).check_data, \
                                     eval(test_table).expect_val,\
                                     eval(test_table).excpect_data_val).all()

                for item in res:
                    parameter_dict = dict()

                    parameter_dict = {key: value if value else "" for key, value in zip(key, item)}

                    test_case_list.append(parameter_dict)

                logging.info(f"test_cases:{test_case_list}")

                return handle_response_data([("data_parameter", test_case_list)])

        if not testcase_number:
            #查询某个模块,某个指令下所有的测试用例

            with db_session() as sess:
                test_table = sess.query(ModulesOrders.module_name,ModulesOrders.order_name).filter(
                    ModulesOrders.module_name_chn == test_module).first()


            test_table_ordername = [item for item in test_table]

            test_table,ordername = test_table_ordername

            with db_session() as sess:
                res = sess.query(eval(test_table).test_no, \
                                     eval(test_table).order_name,\
                                     eval(test_table).is_automation,\
                                     eval(test_table).precondition, \
                                     eval(test_table).test_parmeter,\
                                     eval(test_table).bhcondition,\
                                     eval(test_table).is_check_data,\
                                     eval(test_table).check_data, \
                                     eval(test_table).expect_val,\
                                     eval(test_table).excpect_data_val)\
                            .filter(eval(test_table).order_name == ordername)\
                            .all()

            for item in res:
                parameter_dict = dict()

                parameter_dict = {key: value if value else "" for key, value in zip(key, item)}

                test_case_list.append(parameter_dict)

            logging.info(f"test_cases:{test_case_list}")

            return handle_response_data([("data_parameter", test_case_list)])


        elif testcase_number:
            # 查询某个模块,某条指令下某条测试用例
            with db_session() as sess:
                test_table = sess.query(ModulesOrders.module_name,ModulesOrders.order_name).filter(
                    ModulesOrders.module_name_chn == test_module).first()

            test_table_ordername = [item for item in test_table]

            test_table,ordername = test_table_ordername
            logging.info(f"ordername:{test_table_ordername}")

            with db_session() as sess:
                res = sess.query(eval(test_table).test_no,\
                                     eval(test_table).order_name,\
                                     eval(test_table).is_automation,\
                                     eval(test_table).precondition,\
                                     eval(test_table).test_parmeter,\
                                     eval(test_table).bhcondition,\
                                     eval(test_table).is_check_data,\
                                     eval(test_table).check_data, \
                                     eval(test_table).expect_val,\
                                     eval(test_table).excpect_data_val)\
                                    .filter(eval(test_table)\
                                    .order_name == ordername and eval(test_table)\
                                    .test_no == testcase_number )\
                                    .first()


            parameter_dict = {key: value if value else "" for key, value in zip(key, res)}

            test_case_list.append(parameter_dict)

            logging.info(f"test_cases:{test_case_list}")

            return handle_response_data([("data_parameter", test_case_list)])

# if __name__ == "__main__":
#     find_all_testcases()