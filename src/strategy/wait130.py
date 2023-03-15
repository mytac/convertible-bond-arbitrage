from utils.index import get_data,get_now_date,date_distance,trans_datetime_obj


def filterLowerThanX(date_threshold=365,price_threshold=130):
    data=get_data()
    # print(data)
    now=get_now_date()
    
    for i in range(len(data)):
        cur=data[i]
        ddl_date=trans_datetime_obj(cur['short_maturity_dt'])
        distance=date_distance(ddl_date,now)
        if((distance<=date_threshold) and (cur['price']<price_threshold)):
            # 选出小于180天的
            print(cur['bond_nm'],cur['bond_id'],cur['price'],'还剩:'+str(distance)+' day',cur['ytm_rt'])
        # if()

# 筛选出还有一年到期的，面值小于130的债
def filterLowerThan130():
   filterLowerThanX(365,130)

# 筛选出还有三年到期的，面值小于100的债
def filterLowerThan90():
   filterLowerThanX(365*3,100)