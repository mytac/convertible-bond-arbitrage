from utils.index import get_data,get_now_date,date_distance,trans_datetime_obj


# 正股接近回售套利 x%内
def around_put_convert_price(x=3):
    data=get_data()
    for i in range(len(data)):
      cur=data[i]
      now=get_now_date()
      ddl_date=trans_datetime_obj(cur['maturity_dt'][2:])
      distance=date_distance(ddl_date,now)
      if(cur['put_convert_price'] and cur['sprice'] and distance<365*2.1):
         put_convert_price=cur['put_convert_price']
         sprice=cur['sprice']
         if(sprice<=put_convert_price*(1+x*0.01)):
             print(cur['stock_id']+cur['stock_nm'],'正股现价：'+str(cur['sprice']),'回售价：'+str(cur['put_convert_price']),'距离到期:'+ str(distance)+'天');

