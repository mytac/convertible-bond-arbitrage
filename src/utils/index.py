import json
import numpy
import datetime
from config import output_path

def get_data():
    data=[]
    with open(output_path,'r',encoding='utf-8')as file:
        data=json.load(file)['data']
    return data


# 获取现在日期
def get_now_date():
    now=datetime.datetime.today()
    return now

# 计算两个日期间隔天数
def date_distance(source_date,target_date):
    return source_date.__sub__(target_date).days
# 转换datetime对象
def trans_datetime_obj(date_string,format='%y-%m-%d'):
    return datetime.datetime.strptime(date_string, format)
