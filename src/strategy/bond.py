from utils.index import get_data,get_now_date,date_distance,trans_datetime_obj


# 当前债的面值小于到期赎回价，且到期时间小于 1.1 年，显示年化收益率
def debt_safe_redeem(x=3):
    data=get_data()
    for i in range(len(data)):
      cur=data[i]
      now=get_now_date()
      ddl_date=trans_datetime_obj(cur['maturity_dt'][2:])
      if cur['ytm_rt']:
        distance=date_distance(ddl_date,now)
        if(cur['ytm_rt']>1 and distance<365*x):
          ratio_per_year=cur['ytm_rt']/(distance/365)
          print(cur['bond_id']+cur['bond_nm'],'现面值：'+str(cur['price']),'到期税前收益：'+str(cur['ytm_rt'])+'%','平均年化：'+str(ratio_per_year)+'%','距离到期:'+ str(distance)+'天');