#!/usr/bin/env python
#pip3 install pycoingecko
from pycoingecko import CoinGeckoAPI
import ast

curr='eur'
thre=0.8
principal_coin='btc'

cg=CoinGeckoAPI()
coin_list=cg.get_coins_list()
xx={'btc':'bitcoin','stx':'blockstack'}
for i in coin_list:
    if i['symbol'] not in xx.keys():
        xx[i['symbol']]=i['id']
principal_coin=xx[principal_coin]

#f=open("coins.txt",'a' )
#f.write(str(list))
config_file="/home/disnocen/.config/freefolio/config"  

f=open(config_file,'r')
account_data=f.read()
account_data=ast.literal_eval(account_data)
f.close()
coin_needed=[]

for i in account_data[1:]:
    amounts=i[1]
    for k in amounts.keys():
        if k not in coin_needed:
            coin_needed.append(k)

coinsid=[]
for k in coin_needed:
    coinsid.append(xx[k])
prices=cg.get_price(ids=coinsid,vs_currencies=[curr,'usd'])
print(prices)

for i in account_data[1:]:
    account_name=i[0]
    amounts=i[1]
    coinsid_for=[]
    amountsid={}
    for k in amounts:
        amountsid[xx[k]]=amounts[k]
        coinsid_for.append(xx[k])
    sum=0.0
    principal_partial=0.0
    for i in coinsid_for:
        price=prices[i][curr]
        amount=amountsid[i]
        partial=price*amount
        if (i == principal_coin):
            principal_partial=partial
        sum=sum+partial

    print("total of funds for account",account_name,"is",sum,curr )
    perc=principal_partial/sum
    if perc < thre:
        print("WARNING: the value of",principal_coin,"is",round(perc*100,1),"% which is less than the",thre*100,"% threshold you put. Please rebalance")




