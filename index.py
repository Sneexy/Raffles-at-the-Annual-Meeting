# 获取csv行数 personNum
import csv
personNum = len(open('person.csv','rb').readlines()) - 1

# 生成随机数 randomID
import random
randomID = random.randint(1, personNum) #生成的随机数n: 12 <= n <= 20

# 输出抽到的人的姓名
with open('person.csv','r', encoding='UTF-8') as personName:
    reader = csv.reader(personName)
    result = list(reader)
    print(result[randomID - 1][1])
