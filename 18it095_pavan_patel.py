# -*- coding: utf-8 -*-
"""18IT095_pavan patel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TiaWW9rol2j8tdXcnfezN_E3y0R1o9rH
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url= 'https://www.flipkart.com/search?q=samsung&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
req=requests.get(url)

nm=[]
pr=[]
rt=[]

content=BeautifulSoup(req.content,'html.parser')
print(content)
name=content.find_all('div',{"class":"_4rR01T"})
price= content.find_all('div',{"class":"_g"})
price= content.find_all('div',{"class":"_30jeq3 _1_WHN1"})
rating=content.find_all('div',{"class":"_3LWZIK"})

for i in name:
    nm.append(i.text)
for i in price:
    pr.append(i.text)
for i in rating:
    rt.append(i.text)

data={'NAME':nm,'PRICE':pr,'RATING':rt}
    df=pd.DataFrame(data)
    print(df)
    df.to_csv('18it095_Pavan Patel.csv')