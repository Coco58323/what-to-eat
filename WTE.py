import random
resturant = {"老上海":14,
        "舌尖大师":6,
        "武汉小吃":15,
        "尚千谷":4,
        "五谷鱼粉":9,
        "食誉轩":10,
        "潮蹄":5,
        "牛肉果条":9
        }
count4res = {"老上海":0,
        "舌尖大师":0,
        "武汉小吃":0,
        "尚千谷":0,
        "五谷鱼粉":0,
        "食誉轩":0,
        "潮蹄":0,
        "牛肉果条":1
        }
tot = 0
for k,v in resturant.items():
        tot+=v
cnt=1000
while cnt:
        tmp = random.random()*tot
        for k,v in resturant.items():
                tmp -= v
                if tmp <= 0:
                        count4res[k] += 1
                        break 
        cnt -= 1
print(count4res)