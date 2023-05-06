# convertible-debt-arbitrage

A 股可转债套利，含数据爬取（数据来源集思录），策略等

## 使用

1. 登录集思录，进入[实时数据](https://www.jisilu.cn/web/data/cb/list)，复制你个人的 cookie（chrome 按 F12 打开开发者工具，点击 network，找 headers 中的 cookie，复制）
2. 打开本项目中的[./src/config.py](./src/config.py)替换成你自己的 cookie
3. 在[./src/index.py](./src/index.py)配置策略，直接运行

```py
python ./src/index.py
```

终端会筛选出策略过滤的债

## 策略集合

1. [博 130-当转债还半年到期时，找出面值小于 130 的债 （注意税前到期收益）](./src/strategy/wait130.py)
2. [面值小于 100 时，买入转债（注意正股退市风险）](./src/strategy/wait130.py)
3. [正股接近回售价格 3%内且在到期的 2.1 年内](./src/strategy/stock.py) （23-5-6 新增）

```
配置 around_put_convert_price，运行结果如下

(base) D:\github works\convertible-debt-arbitrage>python ./src/index.py
603278大业股份 现价：8.13 回售价：8.6 距离到期:367天
000700模塑科技 现价：4.93 回售价：5.07 距离到期:26天
002631德尔未来 现价：5.33 回售价：6.03 距离到期:697天
002008大族激光 现价：24.97 回售价：36.25 距离到期:275天
300473德尔股份 现价：15.51 回售价：20.83 距离到期:438天
300297*ST蓝盾 现价：0.48 回售价：0.95 距离到期:464天
```

## data.json 字典

| 字段名             | 含义       |
| ------------------ | ---------- |
| sprice             | 正股价     |
| convert_price      | 转股价     |
| put_convert_price  | 回售触发价 |
| force_redeem_price | 强赎触发价 |
| maturity_dt        | 到期时间   |
