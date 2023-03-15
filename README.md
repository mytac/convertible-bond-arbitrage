# convertible-debt-arbitrage

A 股可转债套利，含数据爬取（数据来源集思录），策略等

## 使用

在[./src/index.py](./src/index.py)配置策略，直接运行

```py
python ./src/index.py
```

终端会筛选出策略过滤的债

## 策略集合

1. [博 130-当转债还半年到期时，找出面值小于 130 的债 （注意税前到期收益）](./src/strategy/wait130.py)
2. [面值小于 100 时，买入转债（注意正股退市风险）](./src/strategy/wait130.py)
