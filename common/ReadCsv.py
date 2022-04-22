#-*-encoding:utf-8-*-
import csv

url=[]


with open("E:\python\project\ApiTest\data\login.csv", "r",encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        url.append(row['url'])
        method=row['method']
    print(url)


