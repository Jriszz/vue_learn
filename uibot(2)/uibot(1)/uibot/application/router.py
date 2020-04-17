from flask import Blueprint
from application.services.modules import get_modules_orders
from application.services.modules.get_modules_orders import get_modules,get_orders
from application.services.modules.get_params import get_order_params
from application.services.modules import get_params
from application.services.testcase import edit_testcase
from application.services.testcase.edit_testcase import add_testcase
from application.services.testcase.find_testcases import find_cases
from application.services.testcase import find_testcases
from application.services.testcase import deploy_testcase
from application.services.testcase.deploy_testcase import deploy_testcases
from application.services.views import view
from application.services.views.view import main_page

'''
:author:zz
:time: 2020/04/11
'''

#创建蓝图块
modules_bp = Blueprint(name=get_modules_orders, import_name='__name__')

modules_bp.add_url_rule("/modules",view_func=get_modules,methods=['GET'])
modules_bp.add_url_rule("/orders",view_func=get_orders,methods=["GET"])

#参数
params_bp = Blueprint(name=get_params,import_name='__name__')

params_bp.add_url_rule("/params",view_func=get_order_params,methods=["GET"])

#测试用例
case_bp = Blueprint(name=edit_testcase,import_name='__name__')
case_bp.add_url_rule("/testcase",view_func=add_testcase,methods=["POST"])

#配置用例
config_case_bp = Blueprint(name=deploy_testcase,import_name='__name__')
config_case_bp.add_url_rule("/casedeploy",view_func=deploy_testcases,methods=["POST"])

#查询用例
find_case_bp = Blueprint(name=find_testcases,import_name='__name__')
find_case_bp.add_url_rule("/testcases",view_func=find_cases,methods=["GET"])

#视图
view_bp = Blueprint(name=view,url_prefix="/index",import_name='__name__')
view_bp.add_url_rule("/main",view_func=main_page,methods=["GET"])