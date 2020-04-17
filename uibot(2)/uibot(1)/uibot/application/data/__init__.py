from sqlalchemy import create_engine
from flask import current_app
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker

from application.utils.configlogger import loger
from application.data.modules import BaseOrders,ModulesOrders


#创建log对象
logging = loger

def engine_create():
    '''
    create database engine
    author: zz
    time: 2020/04/09
    :return:engine
    '''
    engine = create_engine(current_app.config["SQLALCHEMY_DATABASE_URI"],echo=True,pool_recycle=3600)
    return engine

@contextmanager
def db_session():
    '''
    generator db_session managertool
    author :zz
    time:2020/04/09
    :return:
    '''

    try:
        engine = engine_create()
        seesion_db = sessionmaker(bind=engine)
        sess = seesion_db()
        yield sess
    except Exception as err:
        logging.error("数据库连接报错:{}".format(str(err)))
        sess.rollback()
        raise err
    finally:
        logging.debug('关闭数据库会话')
        sess.close()

#转化对象
def to_map(obj):
    return [ table_obj.dobule_to_dict() for table_obj in obj ]




if __name__ == "__main__":
    # USER = "test"
    # PASSWORD = "test"
    # DB_URL = "192.168.0.61:3306"
    # DATABASE_NAME = "testcasedata"
    # engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{DB_URL}/{DATABASE_NAME}?charset=utf8", echo=True, pool_recycle=3600)
    # sess = sessionmaker(bind=engine)()
    # result = sess.query(ModulesOrders).all()
    # print(result)
    pass