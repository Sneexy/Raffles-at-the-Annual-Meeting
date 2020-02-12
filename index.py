# 获取csv行数 personNum
import csv
personNum = len(open('person.csv', 'rb').readlines()) - 1

# 获取奖品数
prizeID = len(open('prizes.csv', 'rb').readlines()) - 1

# 获取抽奖人员名单
with open('person.csv', 'r', encoding='UTF-8') as personName:
    reader = csv.reader(personName)
    result = list(reader)

# 根据奖品列表抽取奖品
## 奖品列表
with open('prizes.csv', 'r', encoding='UTF-8') as personName:
    reader = csv.reader(personName)
    prizes = list(reader)

## 构建数组：已获奖
getPrize = [0] * (personNum + 1) # 有效区间1~personNum

## 抽取随机数
import random

for index1 in range(1, prizeID + 1): # 跳过第一行
    for index2 in range(int(prizes[index1][2])):
        # 生成随机数 randomID
        randomID = random.randint(1, personNum)  # 生成的随机数两边[]
        while getPrize[randomID] == 1:
            randomID = random.randint(1, personNum)
        # 修改数组&输出
        getPrize[randomID] = 1
        print(prizes[index1][0], ' : ', result[randomID][1])