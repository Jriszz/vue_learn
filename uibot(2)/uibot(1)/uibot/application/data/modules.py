from application.data import *
from sqlalchemy import Column,TEXT,String,JSON,Integer,DateTime
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
'''
    @author:zz
    @time: 2020/04/09
'''


# 单个对象
def sing_to_dict(self):
    return {c.name: getattr(self, c.name,None) for c in self.__table__.cloumns}


# 多个对象
def double_to_dict(self):
    '''

    :return: result
    '''

    result = dict()

    return {key: str(getattr(self, key)) if getattr(self, key) else {key: getattr(self, key)} for key in
            self.__mapper__.c.keys()}

Base.sing_to_dict = sing_to_dict
Base.double_to_dict = double_to_dict


class BaseOrders(Base):

    '''
    创建基础命令用例表
    return: None
    '''

    __tablename__ = 'base_orders'

    test_no = Column("TestNo",Integer,primary_key=True,autoincrement=True)
    test_module = Column("TestModule",String(250),nullable=False)
    order_name = Column("OrderName",String(250),nullable=False)
    case_name = Column("CaseName",String(500),nullable=False)
    case_type = Column("CaseType",String(50),default="Normal",nullable=False)
    is_automation = Column("IsAutomation",CHAR(2),default="Y",nullable=False)
    precondition = Column("PreCondition",JSON,nullable=True)
    designer = Column("Designer",String(20),default="admin",nullable=False)
    comments = Column("Comments",String(500),nullable=True)
    bhcondition = Column("BhCondition",JSON,nullable=True)
    is_check_data = Column("IsCheckData",CHAR(2),default="N",nullable=False)
    check_data = Column("CheckData",JSON,nullable=True)
    test_parmeter = Column("TestParmeter",JSON,nullable=True)
    expect_val = Column("ExpectVal",TEXT,nullable=True)
    excpect_data_val = Column("ExpectDataVal", TEXT, nullable=True)
    create_time = Column("CreateTime",DateTime,nullable=True)
    update_time = Column("UpdateTime",DateTime,nullable=True)




class ModulesOrders(Base):

    '''
    创建模块命令关系表
    return: None
    '''

    __tablename__ = "modules_orders"
    module_number = Column("ModuleNumber",Integer,primary_key=True,autoincrement=True)
    module_name = Column("ModuleName",String(250),nullable=True)
    order_name = Column("OrderName",String(250),nullable=True)
    order_name_chn = Column("OrderName_Chn",String(500),nullable=True)
    module_name_chn = Column("ModuleName_Chn",String(250),nullable=True)
    pre_parameter = Column("PreParameter",JSON,nullable=True)
    test_parameter = Column("TestParameter",JSON,nullable=True)
    bh_parameter = Column("BhParameter",JSON,nullable=True)
    table_name = Column("TableName",String(30),nullable=False)

class ExecutionConfiguration(Base):

    '''
    用例配置表
    return None
    '''

    __tablename__ = "exec_config"
    test_sequence = Column("TestSequence",Integer,primary_key=True,autoincrement=True)
    module_name = Column("TestModule",String(250),nullable=False)
    order_name = Column("OrderName", String(250),nullable=False)
    testcase_number =  Column("TestNo",Integer,nullable=True)

# if __name__ == "__main__":
#     with db_session() as sess:
#         result = sess.query(ModulesOrders.module_name,ModulesOrders.order_name).first().sing_to_dict()
#     print(result)