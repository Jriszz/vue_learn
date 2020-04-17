from application.utils.parse_data import handle_request_data,handle_response_data
from application.utils.configlogger import loger
from application.data import db_session
from application.data.modules import ExecutionConfiguration
from flask import current_app

logging = loger

def deploy_testcases():

    '''
    :author: zz
    :time: 2020/04/16
    :return:
    '''
    #配置模块和命令,测试编号等数据

    result = handle_request_data()
    result["testcase_number"] = int(result["testcase_number"]) if result.get("testcase_number","") else 0

    with db_session() as sess:

        res = sess.query(ExecutionConfiguration)\
                    .count()
    logging.info(f"查询配置结果数量：{res}")

    if not res:
        sess.add(ExecutionConfiguration(**result))
        sess.commit()
    else:
        sess.query(ExecutionConfiguration) \
        .filter(ExecutionConfiguration.test_sequence == 1) \
        .update(result)
        sess.commit()

    return handle_response_data()

