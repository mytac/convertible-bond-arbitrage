import json
from bs4 import BeautifulSoup 
import pandas as pd
import requests
from strategy.wait130 import filterLowerThan130,filterLowerThan90
from config import output_path,target_path,cookie



def refresh_data():
   headers={
      'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
      'Cookie':cookie,
      'accept':"application/json, text/plain, */*",
      'columns':"1,70,2,3,5,6,11,12,14,15,16,29,30,32,34,44,46,47,50,52,53,54,56,57,58,59,60,62,63,67",
      'init':'1'
   }

   ret=requests.get(target_path,headers=headers)
   data=ret.json()

  #写入JSON
   with open('./'+output_path,'w',encoding='utf-8')as file:
        file.write(json.dumps(data,ensure_ascii=False))

   #print(data)



def main():
    refresh_data()
    ## 配置策略
    filterLowerThan90()

main()