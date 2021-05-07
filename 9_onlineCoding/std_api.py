import requests
import json
# 新闻
param = {
 'key':'fbde8dccf643050695331fa7d5c78dbd',
 'type':'shehui'
}
res = requests.get(url='http://v.juhe.cn/toutiao/index' ,params=param )
print(type(res.text))
print(res.text)
my_res = json.loads(res.text)
print(my_res['result']['data'])
for info in my_res['result']['data']:
    print(info)



#天气预报


param = {

 'key':'01ec378e6fea5487ac56f403b9745721',
 'cityname':'上海'

}
res = requests.get(url='http://v.juhe.cn/weather/index?key=01ec378e6fea5487ac56f403b9745721&cityname=西安' )
# res = requests.get(url='http://v.juhe.cn/weather/index', params=param)
print(type(res.text))
my_res = json.loads(res.text)
print(my_res['result'])






